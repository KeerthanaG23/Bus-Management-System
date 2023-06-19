const menuBtn = document.getElementById("inline-menu");

// storing sidemenu
const sideMenu = document.getElementById("sidemenu");

// hiding sidemenu at beginning
sideMenu.style.display = "none";

// when side menu btn is clicked
menuBtn.addEventListener("click", function () {
  // disp side menu
  sideMenu.style.display = "flex";
  //   hiding menu btn
  menuBtn.style.display = "none";
});

// creating event to listen to mouse activities in entire window
window.addEventListener("mouseup", function (event) {
  // if user clicks outside sidemenu or on list item inside href
  if (event.target !== sideMenu && event.target.parentNode !== sideMenu) {
    //   hide sidemenu and show menu button
    sideMenu.style.display = "none";
    menuBtn.style.display = "inline";
  }
});
const selected = document.getElementById("selectedfrom");
const fromoptList = document.querySelectorAll(".a");
const fromoptCont = document.querySelector("#fromlist");
const fromoptContainer = document.getElementById("fromlistcont");
const selectedTo = document.getElementById("selectedto");
const tooptCont = document.getElementById("tolist");
const tooptList = document.querySelectorAll(".b");
const tooptContainer = document.getElementById("fromlistcont");
const searchBtn = document.getElementById("searchflt");
const table = document.getElementById("showflt");
table.style.display = "none";

tooptCont.style.display = "none";
fromoptCont.style.display = "none";

selected.addEventListener("click", function () {
  fromoptCont.style.display = "block";
});

selectedTo.addEventListener("click", function () {
  tooptCont.style.display = "block";
});

fromoptList.forEach((element) => {
  element.addEventListener("mouseup", () => {
    selected.innerHTML = element.innerHTML;
    fromoptCont.style.display = "none";
    selected.style.display = "block";
  });
});

tooptList.forEach((element) => {
  element.addEventListener("mouseup", () => {
    selectedto.innerHTML = element.innerHTML;
    tooptCont.style.display = "none";
    selectedto.style.display = "block";
  });
});

searchBtn.addEventListener("click", function () {
  table.style.display = "block";
});

function Upload() {
    var fileUpload = document.getElementById("fileUpload");
    var regex = /^([a-zA-Z0-9\s_\\.\-:])+(.csv|.txt)$/;
    if (regex.test(fileUpload.value.toLowerCase())) {
        if (typeof (FileReader) != "undefined") {
            var reader = new FileReader();
            reader.onload = function (e) {
                var table = document.createElement("table");
                var rows = e.target.result.split("\n");
                for (var i = 0; i < rows.length; i++) {
                    var cells = rows[i].split(",");
                    if (cells.length > 1) {
                        var row = table.insertRow(-1);
                        for (var j = 0; j < cells.length; j++) {
                            var cell = row.insertCell(-1);
                            cell.innerHTML = cells[j];
                        }
                    }
                }
                var dvCSV = document.getElementById("dvCSV");
                dvCSV.innerHTML = "";
                dvCSV.appendChild(table);
            }
            reader.readAsText(fileUpload.files[0]);
        } else {
            alert("This browser does not support HTML5.");
        }
    } else {
        alert("Please upload a valid CSV file.");
    }
}
