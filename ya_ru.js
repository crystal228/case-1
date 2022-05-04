const puppeteer = require('puppeteer');
const URL_TEST = 'https://ya.ru/';

async function testYaRu(){
    console.log('Запуск браузера');
    const browser = await puppeteer.launch({
        headless: false,
        slowMo: 100,
    });
    // todo: создай константу browser и присвой ей результат асинхронного вызова метода launch объекта puppeteer

    console.log('Создание новой вкладки в браузере');
    const page = await browser.newPage();
    // todo: создай константу page и присвоей ей результат асинхронного вызова метода newPage объекта browser

    console.log('Переход на страницу ya.ru');
    await page.goto(URL_TEST);
    // todo: напиши команду перехода на страницу 'https://ya.ru/'

    console.log('Ввод текста "Автоматизация тестирования" в поисковую строку');
    const searchField = await page.$('#text');
    await searchField.type('Автоматизация тестирования');
    // todo: создай константу searchField и присвоей ей результат поиска элемента текстового поля
    // todo: напиши команду ввода в поле текст 'Автоматизация тестирования'

    console.log('Клик в кнопку "Найти"');
    const searchButton = await page.$('.button[type=submit]');
    await searchButton.click();

    console.log('Ожидание перехода в страницу поисковых результатов');
await page.waitForNavigation();
// todo: напиши команду ожидания загрузки результата

console.log('Получение элементов результата поиска');
const result = await page.$('.serp-item');
// todo: создай переменную result и положи в неё элемент поисковой выдачи

console.log('Сравнение ОР и ФР');
if (result==null) {
    console.log('Результаты поиска не найдены');
} else {
    console.log('Результаты поиска отобразились');
}
    // todo: создай константу searchButton и присвоей ей результат поиска элемента кнопки "Найти"
    // todo: напиши команду клика в кнопку поиска

    console.log('Закрытие браузера');
    await browser.close();
    // todo: напиши команду асинхронного закрытия браузера
}

testYaRu();
