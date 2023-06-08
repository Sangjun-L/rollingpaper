function setIsGgamchingMode() {
  sessionStorage.getItem("gammchingMode") === "on"
    ? sessionStorage.setItem("gammchingMode", "off")
    : sessionStorage.setItem("gammchingMode", "on");
  isGgamchingMode();
}

function isGgamchingMode() {
  const body = $('body');
  sessionStorage.getItem("gammchingMode") === "on"
    ? body.addClass("dalcongcongMode")
    : body.removeClass("dalcongcongMode");
}
