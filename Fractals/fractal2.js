
var canvas = document.getElementById("canvas2");        
var context = canvas.getContext("2d");

var CANVAS_SIZE = 500;
var max_iteration = 1000;

//Julia Menge
function drawFractalPoint2(Px,Py){
    // z = (x0 + y0i)
    var x0 = (2*Px)/CANVAS_SIZE-1.5;
    var y0 = (2*Py)/CANVAS_SIZE-1;

    // TODO
    // c ist gegeben, z - variable
    var cy = -0.75;
    var cx = 0.11;
    var iteration = 1;
    var x_temp;
    while ((x0*x0 + y0*y0 < 4) && (iteration < max_iteration)) {
        x_temp = x0*x0 - y0*y0 + cx + x0;
        y0 = 2*x0*y0 + cy + y0;
        x0 = x_temp;                //update of z = z^2 + c
        iteration = iteration + 1;
    }

    color="rgb("+(10*iteration%256)+", "+(10*iteration%256)+", 100)"
    myPoint([Px,Py],color);
}

function drawAll() {
    var factor=2;
    for(var i=0; i < (CANVAS_SIZE/factor);i++)
	   for(var j=0; j < (CANVAS_SIZE/factor);j++)
	       drawFractalPoint2(factor*i,factor*j);
}

function myPoint(pos,color) {
    context.strokeStyle = color;
    context.beginPath();
    context.arc(pos[0],pos[1],1,0,2*Math.PI, true)
    context.closePath()
    context.stroke();
    context.fillStyle = color;
    context.fill();
}

drawAll();
