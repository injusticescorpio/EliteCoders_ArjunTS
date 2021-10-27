var header=$('#details1');

function getRandomColor(){
  var letters = "0123456789ABCDEF";
  var color = '#';
  for (var i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random()*16)];//here will random from 0-16
  }
  return color
}

function changecolor()
{
  colorinput=getRandomColor()
  header.css('color',colorinput)
}
setInterval("changecolor()",500)