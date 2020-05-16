window.onload = function() {
  chart1();
};

function chart() {
  document.getElementById('container1').style.display = 'none';
  document.getElementById("container").style.display = 'block';

  let mychart = document.getElementById("myChart").getContext("2d");

  Chart.defaults.global.defaultFontFamily = "Lato";
  Chart.defaults.global.defaultFontSize = 18;
  Chart.defaults.global.defaultFontColor = "#777";

  let barchart = new Chart(mychart, {
    type: "doughnut", // pie, bar, horizontalbar
    data: {
      labels: [
        "Non Toxic",
        "Toxic",
        "Severe Toxic",
        "Obscene",
        "Threat",
        "Insult",
        "Identity Hate"
      ],
      datasets: [
        {
          label: "Toxicity",
          data: [124473, 15294, 1595, 8449, 478, 7877, 1405],
          backgroundColor: [
            "rgba(255, 99, 132, 0.6)",
            "rgba(54, 162, 235, 0.6)",
            "rgba(153, 102, 255, 0.6)",
            "rgba(255, 206, 86, 0.6)",
            "rgba(150, 10, 200, 0.6)",
            "rgba(255, 159, 64, 0.6)",
            "rgba(200, 150, 150, 0.6)"
          ],
          borderWidth: 0.5,
          borderColor: "#777",
          hoverBorderWidth: 2,
          hoverBorderColor: "#000"
        }
      ]
    },
    options: {
      title: {
        display: true,
        text: "Toxicity Distribution",
        fontSize: 25
      },
      tooltips: {
        enabled: true
      },
      legend: {
        display: true,
        position: "right",
        labels: {
          fontColor: "#000"
        }
      },
      layout: {
        padding: {
          left: 0,
          right: 0,
          bottom: 0,
          top: 0
        }
      }
    }
  });
}

function chart1() {
  document.getElementById('container1').style.display = 'none';
  document.getElementById("container").style.display = 'block';
  console.log("Called");

  let coloR = [];

  let data = [
    "90686",
    "71327",
    "55195",
    "34472",
    "30740",
    "29046",
    "28985",
    "28502",
    "28500",
    "27483",
    "25614",
    "20941",
    "20588",
    "20334",
    "19700",
    "19526",
    "19127",
    "18232",
    "18169",
    "17286",
    "15838",
    "15712",
    "15125",
    "14294",
    "13899",
    "13555",
    "13484",
    "13365",
    "12973",
    "12911",
    "12607",
    "12418",
    "12392",
    "11709",
    "11696",
    "11680",
    "11578",
    "11470",
    "11395",
    "11342",
    "11289",
    "11066",
    "11037",
    "10838",
    "10813",
    "10507",
    "10454",
    "10385",
    "10308",
    "10117"
  ];
  let label = [
    "not",
    "article",
    "page",
    "wikipedia",
    "talk",
    "one",
    "please",
    "would",
    "no",
    "like",
    "dont",
    "see",
    "source",
    "think",
    "also",
    "know",
    "im",
    "time",
    "people",
    "edit",
    "use",
    "make",
    "may",
    "get",
    "say",
    "need",
    "thanks",
    "user",
    "even",
    "name",
    "link",
    "want",
    "good",
    "way",
    "well",
    "information",
    "could",
    "image",
    "go",
    "comment",
    "editor",
    "section",
    "deletion",
    "help",
    "thing",
    "question",
    "first",
    "u",
    "fact",
    "look"
  ];

  let dynamicColors = function() {
    let r = Math.floor(Math.random() * 255);
    let g = Math.floor(Math.random() * 255);
    let b = Math.floor(Math.random() * 255);
    return "rgb(" + r + "," + g + "," + b + ")";
  };

  for (let i in data) {
    coloR.push(dynamicColors());
  }

  let mychart = document.getElementById("myChart").getContext("2d");

  Chart.defaults.global.defaultFontFamily = "Lato";
  Chart.defaults.global.defaultFontSize = 18;
  Chart.defaults.global.defaultFontColor = "#777";

  let barchart = new Chart(mychart, {
    type: "bar", // pie, bar, horizontalbar
    data: {
      labels: label,
      datasets: [
        {
          label: "Occurrence",
          data: data,
          backgroundColor: coloR,
          borderWidth: 0.5,
          borderColor: "#777",
          hoverBorderWidth: 2,
          hoverBorderColor: "#000"
        }
      ]
    },
    options: {
      title: {
        display: true,
        text: "Most Occured Words",
        fontSize: 25
      },
      tooltips: {
        enabled: true
      },
      legend: {
        display: false,
        position: "left",
        labels: {
          fontColor: "#000"
        }
      }
      // layout:{
      //     padding:{
      //         left:0,
      //         right:0,
      //         bottom:0,
      //         top:0
      //     }
      // },
    }
  });
}

function wordCloud() {
  document.getElementById('container1').style.display = 'block';
  document.getElementById("container").style.display = 'none';
  console.log("HERE");
  var dataset = [
    { x: "not", value: 90686 },
    { x: "article", value: 71327 },
    { x: "page", value: 55195 },
    { x: "wikipedia", value: 34472 },
    { x: "talk", value: 30740 },
    { x: "one", value: 29046 },
    { x: "please", value: 28985 },
    { x: "would", value: 28502 },
    { x: "no", value: 28500 },
    { x: "like", value: 27483 },
    { x: "dont", value: 25614 },
    { x: "see", value: 20941 },
    { x: "source", value: 20588 },
    { x: "think", value: 20334 },
    { x: "also", value: 19700 },
    { x: "know", value: 19526 },
    { x: "im", value: 19127 },
    { x: "time", value: 18232 },
    { x: "people", value: 18169 },
    { x: "edit", value: 17286 },
    { x: "use", value: 15838 },
    { x: "make", value: 15712 },
    { x: "may", value: 15125 },
    { x: "get", value: 14294 },
    { x: "say", value: 13899 },
    { x: "need", value: 13555 },
    { x: "thanks", value: 13484 },
    { x: "user", value: 13365 },
    { x: "even", value: 12973 },
    { x: "name", value: 12911 },
    { x: "link", value: 12607 },
    { x: "want", value: 12418 },
    { x: "good", value: 12392 },
    { x: "way", value: 11709 },
    { x: "well", value: 11696 },
    { x: "information", value: 11680 },
    { x: "could", value: 11578 },
    { x: "image", value: 11470 },
    { x: "go", value: 11395 },
    { x: "comment", value: 11342 },
    { x: "editor", value: 11289 },
    { x: "section", value: 11066 },
    { x: "deletion", value: 11037 },
    { x: "help", value: 10838 },
    { x: "thing", value: 10813 },
    { x: "question", value: 10507 },
    { x: "first", value: 10454 },
    { x: "u", value: 10385 },
    { x: "fact", value: 10308 },
    { x: "look", value: 10117 },
    { x: "new", value: 10111 },
    { x: "editing", value: 10057 },
    { x: "work", value: 9941 },
    { x: "point", value: 9858 },
    { x: "discussion", value: 9832 },
    { x: "edits", value: 9702 },
    { x: "thank", value: 9552 },
    { x: "right", value: 9338 },
    { x: "made", value: 9304 },
    { x: "many", value: 9203 },
    { x: "much", value: 9171 },
    { x: "really", value: 9020 },
    { x: "find", value: 8893 },
    { x: "take", value: 8870 },
    { x: "ive", value: 8824 },
    { x: "used", value: 8810 },
    { x: "fuck", value: 8794 },
    { x: "deleted", value: 8703 },
    { x: "reference", value: 8564 },
    { x: "read", value: 8451 },
    { x: "since", value: 8396 },
    { x: "add", value: 8355 },
    { x: "change", value: 8144 },
    { x: "list", value: 8011 },
    { x: "someone", value: 7954 },
    { x: "reason", value: 7833 },
    { x: "still", value: 7703 },
    { x: "policy", value: 7679 },
    { x: "back", value: 7652 },
    { x: "two", value: 7531 },
    { x: "content", value: 7469 },
    { x: "block", value: 7429 },
    { x: "issue", value: 7342 },
    { x: "youre", value: 7336 },
    { x: "year", value: 7302 },
    { x: "mean", value: 7264 },
    { x: "said", value: 7253 },
    { x: "something", value: 7229 },
    { x: "going", value: 7201 },
    { x: "blocked", value: 7196 },
    { x: "state", value: 7195 },
    { x: "case", value: 7170 },
    { x: "stop", value: 7170 },
    { x: "word", value: 7123 },
    { x: "place", value: 7077 },
    { x: "hi", value: 6960 },
    { x: "without", value: 6958 },
    { x: "note", value: 6953 },
    { x: "thats", value: 6818 },
    { x: "problem", value: 6790 }
  ];

  var chart = anychart.tagCloud();
  chart
    .title("Most Common Words")
    .data(dataset)
    .angles([0])
    .colorRange(true);
  chart.colorRange().length("80%");
  chart.container("container1");
  chart.draw();
}