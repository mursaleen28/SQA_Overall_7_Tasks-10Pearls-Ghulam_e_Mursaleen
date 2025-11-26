class HomePage {
    elements = {
        title: () => cy.get('.title'),
        inventoryItems: () => cy.get('.inventory_item'),
    }

    verifyHomePage() {
        this.elements.title().should('have.text', 'Products');
    }

    verifyProductsExist() {
        this.elements.inventoryItems().should('have.length.at.least', 1);
    }
}
 
module.exports = new HomePage();   
