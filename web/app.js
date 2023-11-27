let cash = 0;

function inputCash() {
    cash = parseInt(document.getElementById('cashInput').value);
    if (cash < 500) {
        document.getElementById('message').innerText = '거지에게 제공할 음료는 없습니다';
        document.getElementById('menu').style.display = 'none';
    } else {
        document.getElementById('message').innerText = '어서오세요 고객님 무엇을 도와드릴까요?';
        document.getElementById('menu').style.display = 'block';
    }
}

function order(drink) {
    let price = 0;
    if (drink === '콜라') price = 500;
    else if (drink === '사이다') price = 600;
    else if (drink === '닥터페퍼') price = 700;

    if (cash < price) {
        document.getElementById('message').innerText = '투입한 금액이 부족합니다';
    } else {
        cash -= price;
        document.getElementById('message').innerText = `주문하신 ${drink} 드리겠습니다`;
        document.getElementById('change').innerText = `거스름돈 ${cash}원 드리겠습니다`;
    }
}

function reset() {
    cash = 0;
    document.getElementById('cashInput').value = '';
    document.getElementById('menu').style.display = 'none';
    document.getElementById('message').innerText = '';
    document.getElementById('change').innerText = '';
}
