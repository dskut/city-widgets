/*
  mskfx.js - an open effort to create next generation html5 UX library 
  
  Free to use under the MIT license.
  http://www.opensource.org/licenses/mit-license.php

*/


function mskfx(cb){
this.stop = true;  
this.dbg = true;
this.t = 1;
var that=this;


this.run = function () {
//console.log("run",that);
if(that.stop){return;}
if(that.cb){that.cb(that);}
var c = that.counter;
window.setTimeout(function () { that.run();},that.t*1000);
}

};

