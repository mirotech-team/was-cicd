const express = require('express')
const app = express()
const port = 8080

app.get('/', (req, res) => {
  res.send('Hello Beanstalk!')
})

app.get('/env', (req, res) => {
    res.json(process.env);
  })

app.listen(port, () => {
  console.log(`listening on port ${port}`)
})