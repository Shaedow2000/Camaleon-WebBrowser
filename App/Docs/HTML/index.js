// * reload page
function reloadPageFromCache() {
  window.location.reload();
  console.log("Reload from cache");
  return;
}
console.log("Page Reloaded...");

// * settings button
var settingsBtn = document.getElementById("show-settings");
var settingsSectionPopup = document.getElementById("settings-popup");
var XMark = document.getElementById("x-mark");

function openSettings() {
  document.body.classList.add("settings-on");
  settingsSectionPopup.style.display = "block";
}

function closeSettings() {
  document.body.classList.remove("settings-on");
  settingsSectionPopup.style.display = "none";
}

settingsBtn.addEventListener("click", openSettings);
XMark.addEventListener("click", closeSettings);

// * darkmode/lightmode switch
let darkmode = localStorage.getItem("darkmode");
var modeSwitch = document.getElementById("switch");

const enableDarkmode = () => {
  localStorage.setItem("darkmode", "active");
  document.body.classList.add("darkmode");
  console.log("Changed to dark mode;");
};
const enableLightmode = () => {
  document.body.classList.remove("darkmode");
  console.log("Changed to light mode;");
  localStorage.setItem("darkmode", null);
};

if (darkmode === "active") enableDarkmode();

modeSwitch.addEventListener("click", () => {
  darkmode = localStorage.getItem("darkmode");
  darkmode !== "active" ? enableDarkmode() : enableLightmode();
});

// * change background
var bgOpen = localStorage.getItem("BGCO");
var imgBtn = document.getElementById("bg-switch");
var imgsPopup = document.getElementsByClassName("bg-changer");

const openBgChanger = () => {
  document.body.classList.add("bg-changer-open");
  localStorage.setItem("BGCO", "active");
};
const closeBgChanger = () => {
  document.body.classList.remove("bg-changer-open");
  localStorage.setItem("BGCO", null);
};

if (bgOpen === "active") openBgChanger();

imgBtn.addEventListener("click", () => {
  bgOpen = localStorage.getItem("BGCO");
  bgOpen !== "active" ? openBgChanger() : closeBgChanger();
});

// ? change bg: showed
var openSolidColors = document.getElementById("openSolid-colors");
var openAbstArt = document.getElementById("openAbstract-art");
var openSolidShapes = document.getElementById("openSolid-shapes");
var openImgs = document.getElementById("openImages");

const openColorsSec = () => {
  document.body.classList.add("openSolid");
  localStorage.setItem("ColorsSec", "active");
}
const closeColorsSec = () => {
  document.body.classList.remove("openSolid");
  localStorage.setItem("ColorsSec", null);
}
if (localStorage.getItem("ColorsSec") === "active") openColorsSec();

const openAbstArtSec = () => {
  document.body.classList.add("openAbstArt");
  localStorage.setItem("AbstArtSec", "active");
}
const closeAbstArtSec = () => {
  document.body.classList.remove("openAbstArt");
  localStorage.setItem("AbstArtSec", null);
}
if (localStorage.getItem("AbstArtSec") === "active") openAbstArtSec();

const openShapesSec = () => {
  document.body.classList.add("openShp");
  localStorage.setItem("ShapesSec", "active");
}
const closeShapesSec = () => {
  document.body.classList.remove("openShp");
  localStorage.setItem("ShapesSec", null);
}
if (localStorage.getItem("ShapesSec") === "active") openShapesSec();

const openImagesSec = () => {
  document.body.classList.add("openImg");
  localStorage.setItem("ImagesSec", "active");
}
const closeImagesSec = () => {
  document.body.classList.remove("openImg");
  localStorage.setItem("ImagesSec", null);
}
if (localStorage.getItem("ImagesSec") === "active") openImagesSec();

openSolidColors.addEventListener("click", () => {
  ColorsSec = localStorage.getItem("ColorsSec");
  ColorsSec !== "active" ? openColorsSec() : closeColorsSec();
});
openAbstArt.addEventListener("click", () => {
  abstartSec = localStorage.getItem("AbstArtSec");
  abstartSec !== "active" ? openAbstArtSec() : closeAbstArtSec();
});
openSolidShapes.addEventListener("click", () => {
  shapesSec = localStorage.getItem("ShapesSec");
  shapesSec !== "active" ? openShapesSec() : closeShapesSec();
});
openImgs.addEventListener("click", () => {
  imagesSec = localStorage.getItem("ImagesSec");
  imagesSec !== "active" ? openImagesSec() : closeImagesSec();
});

// * chage background functions
const changeBg = (bg, colorOrNo) => {
  if (colorOrNo === true) {
    var Bg = getComputedStyle(bg);
    document.documentElement.style.cssText = "--background: " + Bg.background;
  } else {
    var suffixBg = bg.replace("http://127.0.0.1:5500/Python/WebBrowser/WebBrowser-Name/App/Docs", "..");
    document.documentElement.style.cssText = "--background: url('" + suffixBg + "');";
  }
}

// * search bar mecanics
document
  .getElementById("searchForm")
  .addEventListener("submit", function (event) {
    var query = this.q.value.trim();
    if (!query) {
      console.warn("WARNING: No value detected in the input field.");
      event.preventDefault();
    }
  });

// * function for search engine link
searchForm = document.getElementById("searchForm");
var googleIcon = window.getComputedStyle(
  document.getElementById("google-icon")
).display;

var braveIcon = window.getComputedStyle(
  document.getElementById("brave-search-icon")
).display;

var bingIcon = window.getComputedStyle(
  document.getElementById("bing-search-icon")
).display;

var duckduckgoIcon = window.getComputedStyle(
  document.getElementById("duckduckgo-search-icon")
).display;

var searchEngineLink = document.getElementById("search-engine-link");

var google = document.getElementById("google-icon");
var brave = document.getElementById("brave-search-icon");
var bing = document.getElementById("bing-search-icon");
var duckduckgo = document.getElementById("duckduckgo-search-icon");

const changeSearchEngine = () => {
  if (googleIcon === "block") {
    searchEngineLink.removeAttribute("href");
    searchEngineLink.setAttribute("href", "https://www.google.com/");
    searchForm.removeAttribute("action");
    searchForm.setAttribute("action", "https://www.google.com/search");
    console.log("Changed search engine to 'https://www.google.com/'");
  } else if (braveIcon === "block") {
    searchEngineLink.removeAttribute("href");
    searchEngineLink.setAttribute("href", "https://search.brave.com/");
    searchForm.removeAttribute("action");
    searchForm.setAttribute("action", "https://search.brave.com/search");
    console.log("Changed search engine to 'https://search.brave.com/'");
  } else if (bingIcon === "block") {
    searchEngineLink.removeAttribute("href");
    searchEngineLink.setAttribute("href", "https://www.bing.com/");
    searchForm.removeAttribute("action");
    searchForm.setAttribute("action", "https://www.bing.com/search");
    console.log("Changed search engine to 'https://www.bing.com/'");
  } else if (duckduckgoIcon === "block") {
    searchEngineLink.removeAttribute("href");
    searchEngineLink.setAttribute("href", "https://www.duckduckgo.com/");
    searchForm.removeAttribute("action");
    searchForm.setAttribute("action", "https://duckduckgo.com/");
    console.log("Changed search engine to 'https://www.duckduckgo.com/'");
  } else {
    searchEngineLink.removeAttribute("href");
    searchEngineLink.setAttribute("href", "https://www.google.com/");
    searchForm.removeAttribute("action");
    searchForm.setAttribute("action", "https://www.google.com/search");
    console.log("Changed search engine to 'https://www.google.com/'");
    google;
  }
};

window.onload = changeSearchEngine();
