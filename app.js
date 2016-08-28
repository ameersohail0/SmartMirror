var check = 0;

var cleaner = function()
{

	var PythonShell = require('python-shell');
 
	var options = {
    	mode: 'text',
		scriptPath: './src/',
  		args: []
	};

	PythonShell.run('cleaner.py',options,function(err,results){
		if (err) throw err;
		console.log('results: %j',results);
		checkUser();
	});

};

var recognizeUser = function()
{
	var PythonShell = require('python-shell');
 
	var options = {
    	mode: 'text',
		scriptPath: './src/',
  		args: []
	};

	PythonShell.run('faceRecognizer.py',options,function(err,results){
		if (err) throw err;
		console.log('results: %j',results);
		console.log('recognized');
		cleaner();
	});

};

var verifyUser = function()
{

	var PythonShell = require('python-shell');
 
	var options = {
    	mode: 'text',
		scriptPath: './src/',
  		args: []
	};

	check = 1;
 
	PythonShell.run('faceDetectAndCapture.py', options, function (err, results) {
	if (err) throw err;
	
	// results is an array consisting of messages collected during execution 
	
  	//console.log('results: %j', results);
	
	if(results[0].toString() == "done")
		{console.log('its working,, i know');
		check = 0;
		recognizeUser(); }

	});

};

var checkUser = function()
{
	if (check == 0)
	{ verifyUser();	};
};

//setInterval(checkUser,120000);
cleaner();
