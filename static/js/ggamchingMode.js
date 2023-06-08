function setIsGgamchingMode() {
  localStorage.getItem('gammchingMode') === 'on'
    ? localStorage.setItem('gammchingMode', 'off')
    : localStorage.setItem('gammchingMode', 'on');
  isGgamchingMode();
}

function isGgamchingMode() {
  const body = $('body');
  localStorage.getItem('gammchingMode') === 'on'
    ? body.addClass('dalcongcongMode')
    : body.removeClass('dalcongcongMode');
}
