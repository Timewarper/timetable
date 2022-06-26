import random

def swap(array, index_x, index_y):
    temp = array[index_x]
    array[index_x] = array[index_y]
    array[index_y] = temp
    return array

def timetable(students):
    class_count = []
    for i in range(5):
        cc = []
        for student in students:
            if student[i] not in [cc[i][0] for i in range(len(cc))]:
                cc.append([student[i], 1])
            else:
                cc[[cc[i][0] for i in range(len(cc))].index(student[i])][1] += 1
        class_count.append(cc)

    for c in class_count:
        for i in range(len(c)-1):
            rems = []
            if c[i][0] == '':
                rems.append(i)
            for rem in rems:
                c.pop(i)
    return class_count

def subj_numbers(students):
    cc = []
    for i in range(5):
        for student in students:
            if student[i] not in [cc[i][0] for i in range(len(cc))]:
                cc.append([student[i], 1])
            else:
                cc[[cc[i][0] for i in range(len(cc))].index(student[i])][1] += 1

    for i in range(len(cc)):
        rems = []
        if cc[i][0] == '':
            rems.append(i)
        for rem in rems:
            cc.pop(i)
    return cc


def score_assign(lesson_list, class_nums):
    score = 0
    # Checks to be made
    # Class sizes: [10-25 for Sci, Humanities, Mod Langs, Latin, Computing, PE], [8-12 for DT, 3D], [1 class for Art, Drama, Music, Greek]
    small_classes = ["3D Design", "DT"]
    one_class = ["Art","Drama","Music","Greek","Chinese"]
    one_class_nums = [0 for i in range(len(one_class))]
    other_classes = []
    other_classes_expected = []
    # Index corresponds, format: [number_of_classes, students_per_class]
    for c in class_nums:
        if c[0] not in one_class and c[0] not in small_classes:
            other_classes.append(c[0])
            number_of_classes = ((c[1] - 1) // 24) + 1
            if c[0] in ["German", "Triple Science"]:
                number_of_classes += 1
            elif c[0] == "Spanish":
                number_of_classes -= 1
            other_classes_expected.append([number_of_classes,c[1]/number_of_classes])

    other_class_nums = [0 for i in range(len(other_classes))]

    for slot in lesson_list:
        for lesson in slot:
            if lesson[0] in one_class:
                one_class_nums[one_class.index(lesson[0])] += 1
            elif lesson[0] in small_classes:
                if lesson[1] > 12 or lesson[1] < 8:
                    score += min(abs(lesson[1]-25),abs(lesson[1]-10))
            else:
                if lesson[0] == "":
                    pass
                else:
                    other_class_nums[other_classes.index(lesson[0])] += 1
                    lowerBound = max(10, round(other_classes_expected[other_classes.index(lesson[0])][1] * 0.8))
                    upperBound = min(24, round(other_classes_expected[other_classes.index(lesson[0])][1] * 1.2))
                    if lesson[0] == "Spanish":
                        upperBound = 25
                    #lesson[1] < lowerBound or
                    if lesson[1] > upperBound:
                        score += abs(lesson[1] - upperBound)
                        # min(abs(lesson[1] - lowerBound),)

    for num in one_class_nums:
        score += (num-1) * 50

    for i in range(len(other_class_nums)):
        score += abs(other_class_nums[i]-other_classes_expected[i][0]) * 50

    return score



def main(subjs_list):
    bestScore = 200000
    class_nums = subj_numbers(subjs_list)
    classes = timetable(subjs_list)
    score = score_assign(classes, class_nums)
    print(score)
    print(subjs_list)
    for i in range(len(subjs_list)):
        if "Art" in subjs_list[i]:
            subjs_list[i] = swap(subjs_list[i], 0, subjs_list[i].index("Art"))
        elif "Drama" in subjs_list[i]:
            subjs_list[i] = swap(subjs_list[i], 1, subjs_list[i].index("Drama"))
        elif "Music" in subjs_list[i]:
            subjs_list[i] = swap(subjs_list[i], 2, subjs_list[i].index("Music"))
        elif "Chinese" in subjs_list[i]:
            subjs_list[i] = swap(subjs_list[i], 3, subjs_list[i].index("Chinese"))
    bestSubjList = subjs_list
    print(subjs_list)
    while bestScore != 0:
        subjs_list = bestSubjList
        if bestScore >= 2000:
            times = bestScore//20
        elif bestScore >= 1500:
            times = bestScore // 40
        elif bestScore >= 1000:
            times = bestScore // 100
        else:
            times = 5
        for j in range(round(times)):
            i = random.randint(0,141)
            swap(subjs_list[i], random.randint(0,4), random.randint(0,4))
        for i in range(len(subjs_list)):
            if "Art" in subjs_list[i]:
                subjs_list[i] = swap(subjs_list[i], 0, subjs_list[i].index("Art"))
            elif "Drama" in subjs_list[i]:
                subjs_list[i] = swap(subjs_list[i], 1, subjs_list[i].index("Drama"))
            elif "Music" in subjs_list[i]:
                subjs_list[i] = swap(subjs_list[i], 2, subjs_list[i].index("Music"))
            elif "Chinese" in subjs_list[i]:
                subjs_list[i] = swap(subjs_list[i], 3, subjs_list[i].index("Chinese"))
        classes = timetable(subjs_list)
        score = score_assign(classes,class_nums)
        if score < bestScore:
            best = classes
            bestScore = score
            bestSubjList = subjs_list
            print(classes)
            for i in range(5):
                print(f"Slot {i + 1}")
                print("-" * 10)
                for c in best[i]:
                    print(f"{c[0]}: {c[1]}")
                print()
            print(score)