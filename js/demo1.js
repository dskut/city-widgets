(function() {
var fx_counter = 0;

// new mskfx object 
var fx1 = new mskfx();

fx1.cb = function(c){
  fx_counter=fx_counter+1;console.log("counter",fx_counter);
  if (fx_counter>=5){c.stop=true;}
  
};


// start !!!
fx1.run();


})();

