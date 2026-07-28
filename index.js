
const express = require('express');
const axios = require('axios');

const app = express();

app.get('/', (req, res) => {
	res.json({ message: 'Hello from Express scaffold!' });
});

function runSelfTest() {
	const server = app.listen(3000, async () => {
		try {
			const resp = await axios.get('http://localhost:3000/');
			console.log('Express self-test status:', resp.status);
			console.log('Express self-test body:', resp.data);
		} catch (err) {
			console.error('Express self-test error:', err.message);
		} finally {
			server.close();
		}
	});
}

if (require.main === module) {
	runSelfTest();
}
