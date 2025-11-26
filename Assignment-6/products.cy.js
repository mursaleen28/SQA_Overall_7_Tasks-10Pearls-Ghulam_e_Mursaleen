const LoginPage = require('./pages/LoginPage');
const HomePage = require('./pages/HomePage');

describe('Product Navigation & Validation', () => {
    it('Should display products after login', () => {
        // Login page visit aur login
        LoginPage.visit();
        LoginPage.login('standard_user', 'secret_sauce');

        // Home page validations
        HomePage.verifyHomePage();
        HomePage.verifyProductsExist();
    });
});     
