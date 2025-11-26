describe('SauceDemo Login Tests', () => {

  it('Login Failure Test', () => {
    cy.visit('https://www.saucedemo.com/');
    cy.get('#user-name').type('wrongUser');
    cy.get('#password').type('wrongPass');
    cy.get('#login-button').click();

    cy.get('[data-test="error"]').should('be.visible');
  });

  it('Login Success Test', () => {
    cy.visit('https://www.saucedemo.com/');
    cy.get('#user-name').type('standard_user');
    cy.get('#password').type('secret_sauce');
    cy.get('#login-button').click();

    cy.url().should('include', '/inventory.html');
  });

}); 
  