const express = require('express');
const cors = require('cors');
const basicAuth = require('express-basic-auth');

const app = express();

app.use(cors());
app.use(
	basicAuth({
		users: { ADMIN: 'test' },
	})
);

app.listen(8000, () => console.log('Listening on port 8000'));

app.get('/', async (req, res) => {
	try {
		res.status(200).json('Hello World');
	} catch (err) {
		console.log(err);
		res.status(500).send('Server Error');
	}
});

// curl -u ADMIN:test http://localhost:8000
