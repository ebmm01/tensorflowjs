let express = require("express");
let app = express();

app.use(function(req, res, next) {
    console.log(`${new Date()} - ${req.method} request for ${req.url}`);
    next();
})

//var directory = require('serve-index');
//app.use(directory(__dirname + '/static'));
app.use(express.static(__dirname + '/static'));

app.listen(8080, function() {
    console.log("Serving static on :8080");
})