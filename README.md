# Test-task-Loyalty-program-API

App on Heroku:
https://test-task-loyalty-program-api.herokuapp.com/loyalty/

todo:
- додати аутинтефікацію, щоб баланси клієнтів показувалися лише для рахунків підприємства партнера, по якому здійснюється вхід до API
- приховати секретний ключ, виключити дебаг



Бізнес-постановка:

Ваша компанія створює сервіс для автоматизації програм лояльності. Ваші клієнти — заклади, в яких є валсні програми лояльності, але яким дорого/не вигідно утримувати власний штат ІТ. 

На даний момент, ви запускаєте сервіс, який дозволяє користувачам накопичувати бали, за ті, чи інші послуги. Вам слід реалізувати АРІ (яке ви в подальшому передасте в користування вашим партнерам), яке реалізовує наступну бізнес-механіку: 1) додання балів до рахунку користувача з вказанням опису послуги та збереженням дати, коли відбулось начисилення. 2) аналогічним чином реалзова списання балів. 3) поточний баланс.

Крім цього, вашим клієнтам важливо мати деяку статистику по сервісу: їм потрібні нотифікації в реальному часі про клієнтів, які накопичили більше 1000 балів, та про тих, які використали всі бали і тепер їх баланс дорівнює 0. Також, важливо отримувати нотифікації, яка загальна сума всіх накопичених бонсуів перевищує 100к.

Опис з точки зору ІТ:
Ваша ІТ-інфраструктура передбачає чіткий поділ на мікро-сервіси. Вам слід реалізувати 2 мікросервіси: 

**1-й МС повинен відповідити за облік балансів коирстувачів. В його основі повинен бути postgres та django-логіка, яка реалізує АРІ для начислення/списвання коштів, а також метод баласну.**

2-й МС повинен бути побудований на основі Celery та Clickhouse. Celery-based логіка повинна раз в хвилину підраховувати загальний баланс і писати його в clickhouse таким чином, щоб накопиувати статистику коливань загального балансу в часі. Крім цього, при зміні балансу того чи іншого користувача, даний сервіс повинен автоматично проводити перевірку на предмет 0/1000 балів.
