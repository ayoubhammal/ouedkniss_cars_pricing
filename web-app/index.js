const express = require('express');
const path = require('path');
const volleyball = require('volleyball');

const app = express();
const port = 3000;

// View engine
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

// Middleware
app.use(volleyball);
app.use('/assets', express.static(path.join(__dirname, 'public')));


// Routes
app.get('/', (req, res) => {
  res.render('index');
});
app.get('/about', (req, res) => {
  res.render('about');
});

// Errors handling
function notFound(req, res, next) {
  res.status(404);
  const error = new Error('Not Found - ' + req.originalUrl);
  next(error);
}

function errorHandler(err, req, res, next) {
  if (err)
    console.log(err);
  res.status(res.statusCode || 500);
  res.render('404');
}

app.use(notFound);
app.use(errorHandler);

// Listening
app.listen(port, () => {
  console.log(`Listening at http://localhost:${port}`);
});