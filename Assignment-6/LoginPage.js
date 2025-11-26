class LoginPage {
    elements = {
        username: () => cy.get('#user-name'),
        password: () => cy.get('#password'),
        loginBtn: () => cy.get('#login-button'),
        errorMsg: () => cy.get('[data-test="error"]')
    }

    visit() {
        cy.visit('https://www.saucedemo.com/');
    }

    login(username, password) {
        this.elements.username().type(username);
        this.elements.password().type(password);
        this.elements.loginBtn().click();
    }
} 

module.exports = new LoginPage();  
