// * setting: change search engine
localStorage.setItem("opened", null);
var opened = localStorage.getItem("opened");
var settingBtn = document.getElementById("switch-engine");
var settingSectionPopup = document.getElementById("engine-popup");

const openSetting = () => {
  localStorage.setItem("opened", "active");
  document.body.classList.add("opened");
};
const closeSetting = () => {
  localStorage.setItem("opened", null);
  document.body.classList.remove("opened");
};

if (opened === "active") openSetting();

settingBtn.addEventListener("click", () => {
  opened = localStorage.getItem("opened");
  opened !== "active" ? openSetting() : closeSetting();
});

// ? change search engine buttons
var googleBtn = document.getElementById("google-sec");
var bingBtn = document.getElementById("bing-sec");
var braveBtn = document.getElementById("brave-sec");
var duckduckgoBtn = document.getElementById("duckduckgo-sec");

function changeEngine(engineName) {
  console.log("it works fine...");
}

googleBtn.addEventListener("click", changeEngine("google"));
braveBtn.addEventListener("click", changeEngine("brave"));
bingBtn.addEventListener("click", changeEngine("bing"));
duckduckgoBtn.addEventListener("click", changeEngine("duckduckgo"));
