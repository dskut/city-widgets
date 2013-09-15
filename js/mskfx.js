/*
  mskfx.js - an open effort to create next generation html5 UX library 
  
  Free to use under the MIT license.
  http://www.opensource.org/licenses/mit-license.php

*/


function mskfx(cb){
this.stop = true;  
this.t = 1;
var that=this;


this.run = function () {
if(that.stop){return;}
if(that.cb){that.cb(that);}
var c = that.counter;
window.setTimeout(function () { that.run();},that.t*1000);
}

};

