let items = document.querySelectorAll('.bgslider .list .item');
let next = document.getElementById('next');
let prev = document.getElementById('prev');
let itemActive = Math.floor(Math.random() * 8);
let countItem = items.length;

next.onclick = function(){
    itemActive += 1;
    if(itemActive>=countItem){
        itemActive = 0;
    }
    showSlider();
}
prev.onclick = function(){
    itemActive -= 1;
    if(itemActive<0){
        itemActive = countItem;
    }
    showSlider();
}
next.click();
let refreshInterval = setInterval(()=>{
    next.click();
},10000)

function showSlider(){
    let itemActiveOld = document.querySelector('.bgslider .list .item.active');
    itemActiveOld.classList.remove('active');
    items[itemActive].classList.add('active');

    clearInterval(refreshInterval);
    refreshInterval = setInterval(()=>{
        next.click();
    },10000)
}
