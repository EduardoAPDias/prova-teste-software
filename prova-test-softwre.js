const { Builder, By } = require('selenium-webdriver'); //importa os modulos necessesarios

//Função testehanked
(async function testeHanked() {
const url = 'https://www.hankeds.com.br/prova/login2.html'; //define URL
let driver = await new Builder().forBrowser('chrome').build(); //Inicia chromedriver

try {

await driver.get(url); //Acessa pagina
await driver.sleep(2000); //espera

//localiza os campos usuario e senha por id e o botão por xpath
const username = await driver.findElement(By.id('username'));
const password = await driver.findElement(By.id('password'));
const botao = await driver.findElement(By.xpath("//button[contains(text(),'Entrar')]"));

// digita admin esperando entre as letras
for (const letra of 'admin') {
await username.sendKeys(letra);
await driver.sleep(250);
}

await driver.sleep(1000); // espera

// digita senha esperando entre as letras
for (const letra of 'admin123456') {
await password.sendKeys(letra);
await driver.sleep(250);
}

// espera e clica no botão
await driver.sleep(1000); 
await botao.click();

await driver.sleep(4000); //espera

const urlAtual = await driver.getCurrentUrl(); // pega a URL da pagina

//faz a verificação do teste
if (urlAtual.includes('destino.html')) {
console.log(' Teste passou: redirecionado corretamente.');
} else {
console.log(' Teste falhou: não houve redirecionamento.');
}

await driver.sleep(5000); //espera

//se houver erro avisa no console
} catch (err) {
console.error(' Erro durante o teste:', err);
} finally {
await driver.quit();
}
})();