let data = require("./data.json");

let MAX_SLOTS = 5; // classes per day
let MAX_KIDS = 24;

let subjectSlots = [];
// example subject looks like this: "Physics": 2

let output = [{}];
// heirarchy - day -> slot -> ...studentIDs

// go through all the "students"
for (let ID = 0; ID < data.length; ID++) {
  let student = data[ID];
  // console.log("> iter", ID, "-", student);
  // go through subjects taken by student
  for (let j = 0; j < student.length; j++) {
    let subject = student[j];

    // console.log(">>", subject);

    // check if subject is "" (nothing)
    if (subject == "") {
      // console.log("lazy kid huh");
      student.splice(j--, 1);
      continue;
    }


    // update the latest slot for specific subject
    if (subjectSlots[subject] == undefined) {
      subjectSlots[subject] = output.length - 1;
    }

    // last slot
    let lastSlot;
    if (output[subjectSlots[subject]] >= MAX_KIDS) {
      lastSlot = output[output.length - 1];
      // update the slot the subject is on
      subjectSlots[subject] = output.length - 1;
    } else lastSlot = output[subjectSlots[subject]];
    // console.log(">> last slot -", lastSlot);
    // console.log(">> subject slot -", subjectSlots);

    // if slot is full, skip this
    if (Object.keys(lastSlot).length > MAX_SLOTS) {
      output.push({});
      output[output.length - 1][subject] = [];
      subjectSlots[subject] = output.length - 1;
      j--;
      continue;
    }

    // console.log(">> last slot", j, "-", lastSlot);
    // if not set, set subject slot 
    lastSlot[subject] ??= [];


    // don't do anything if class is full
    // if (lastSlot[subject].length < MAX_KIDS) {
    lastSlot[subject].push(ID);
    // }
    student.splice(j--, 1);
  }
  // console.log("-- output:", output);

}

console.log(output);