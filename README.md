# timetable
A collection of timetable algorithms for a project, designed to help improve the welfare and wellbeing of the general students at our school by voluntarily transferring intellectual property to ensure a better experience for everyone. (haha just kidding we harvested everyone's data and used it for some questionable things)

The only current working scripts are data.json.

Aim of the project: To produce a working timetable, given a list of students and their choices. Teachers and rooms will be ignored for all working purposes in this setting.

Slots will represent four periods in a week, since all subjects require the same amount of time and if any one pupil has a subject in one period, they will also have it in the other three corresponding periods in that "slot". This is to simplify the problem. There are 5 such "slots" in a week.

Certain constraints will be applied to limit options. The code will most likely not be NP-Complete due to a lack of ideas regarding how to efficiently code a solution that doesn't take more than a day to run.
