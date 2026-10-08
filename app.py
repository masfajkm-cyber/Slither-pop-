import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
page_title="SlitherPop",
page_icon="🐍"
)

components.html("""

<!DOCTYPE html>  <html>  
<head>  <style>  
  
* {  
    box-sizing: border-box;  
}  
  
body {  
    margin: 0;  
    background: white;  
    font-family: Arial, sans-serif;  
    text-align: center;  
    color: #b1124a;  
}  
  
.title {  
    font-size: 40px;  
    font-weight: 900;  
    margin-top: 4px;  
}  
  
.by {  
    font-size: 15px;  
    font-weight: 600;  
    margin-bottom: 12px;  
}  
  
/* CUSTOMIZATION PANEL */  
  
.custom-panel {  
    max-width: 380px;  
    margin: auto;  
    background: #f8c8dc;  
    border-radius: 22px;  
    padding: 14px;  
}  
  
.custom-title {  
    font-size: 18px;  
    font-weight: 800;  
    margin-bottom: 8px;  
}  
  
.choice-row {  
    display: flex;  
    justify-content: center;  
    gap: 10px;  
    flex-wrap: wrap;  
}  
  
.choice {  
    border: 3px solid transparent;  
    background: white;  
    border-radius: 15px;  
    padding: 8px 12px;  
    font-size: 15px;  
    font-weight: bold;  
    color: #b1124a;  
    cursor: pointer;  
}  
  
.choice.selected {  
    border-color: #b1124a;  
    background: #ffe1ed;  
}  
  
/* SCORE */  
  
.score {  
    font-size: 22px;  
    font-weight: 900;  
    margin: 10px;  
}  
  
/* GAME */  
  
canvas {  
    width: min(90vw, 360px);  
    height: min(90vw, 360px);  
    background: #fff4f8;  
    border: 5px solid #b1124a;  
    border-radius: 24px;  
    display: block;  
    margin: auto;  
}  
  
/* CONTROLS */  
  
.controls {  
    width: 220px;  
    margin: 13px auto;  
    display: grid;  
    grid-template-columns: repeat(3, 1fr);  
    gap: 8px;  
}  
  
.control {  
    height: 55px;  
    border: none;  
    border-radius: 17px;  
    background: #f4a9c4;  
    color: #b1124a;  
    font-size: 25px;  
    font-weight: bold;  
    touch-action: manipulation;  
}  
  
.control:active {  
    transform: scale(.93);  
    background: #e88aaa;  
}  
  
/* RESTART */  
  
.restart {  
    border: none;  
    border-radius: 16px;  
    background: #b1124a;  
    color: white;  
    padding: 13px 30px;  
    font-size: 18px;  
    font-weight: 900;  
    cursor: pointer;  
    margin-bottom: 18px;  
}  
  
.restart:active {  
    transform: scale(.95);  
}  
  
.empty {  
    visibility: hidden;  
}  
  
</style>  </head>  <body>  <div class="title">SlitherPop</div>  
<div class="by">by Masfa</div>  <!-- CUSTOMIZATION -->  <div class="custom-panel">  <div class="custom-title">  
    🐍 Choose Your Snake  
</div>  

<div class="choice-row">  

    <button class="choice selected" data-color="#e05283">  
        🩷 Pink  
    </button>  

    <button class="choice" data-color="#e53935">  
        ❤️ Red  
    </button>  

    <button class="choice" data-color="#2196f3">  
        💙 Blue  
    </button>  

    <button class="choice" data-color="#4caf50">  
        💚 Green  
    </button>  

    <button class="choice" data-color="#9c27b0">  
        💜 Purple  
    </button>  

    <button class="choice" data-color="#111111">  
        🖤 Black  
    </button>  

</div>  

<br>  

<div class="custom-title">  
    🍎 Choose Your Food  
</div>  

<div class="choice-row">  

    <button class="choice food selected" data-food="🍎">  
        🍎 Apple  
    </button>  

    <button class="choice food" data-food="🍓">  
        🍓 Berry  
    </button>  

    <button class="choice food" data-food="🍒">  
        🍒 Cherry  
    </button>  

    <button class="choice food" data-food="🍕">  
        🍕 Pizza  
    </button>  

    <button class="choice food" data-food="🍩">  
        🍩 Donut  
    </button>  

    <button class="choice food" data-food="🍉">  
        🍉 Melon  
    </button>  

</div>

</div>  <div class="score" id="score">  
    🏆 Score: 0  
</div>  <canvas id="game" width="360" height="360"></canvas>

<!-- MOBILE CONTROLS -->  <div class="controls">  <div class="empty"></div>  

<button class="control" id="up">  
    ⬆️  
</button>  

<div class="empty"></div>  

<button class="control" id="left">  
    ⬅️  
</button>  

<button class="control" id="down">  
    ⬇️  
</button>  

<button class="control" id="right">  
    ➡️  
</button>

</div>  <button class="restart" id="restart">  
    🔄 Restart Game  
</button>  <script>  
  
const canvas = document.getElementById("game");  
const ctx = canvas.getContext("2d");  
  
const grid = 18;  
const cell = 20;  
  
let snake;  
let direction;  
let nextDirection;  
let food;  
let foodEmoji = "🍎";  
let snakeColor = "#e05283";  
let score = 0;  
let gameOver = false;  
  
  
/* =========================  
   GAME START  
========================= */  
  
function restart() {  
  
    snake = [  
        {x: 9, y: 9},  
        {x: 8, y: 9},  
        {x: 7, y: 9},  
        {x: 6, y: 9}  
    ];  
  
    direction = {  
        x: 1,  
        y: 0  
    };  
  
    nextDirection = {  
        x: 1,  
        y: 0  
    };  
  
    score = 0;  
    gameOver = false;  
  
    document.getElementById("score").textContent =  
        "🏆 Score: 0";  
  
    createFood();  
  
    draw();  
}  
  
  
/* =========================  
   FOOD  
========================= */  
  
function createFood() {  
  
    food = {  
        x: Math.floor(Math.random() * grid),  
        y: Math.floor(Math.random() * grid)  
    };  
  
}  
  
  
/* =========================  
   DIRECTION  
========================= */  
  
function changeDirection(x, y) {  
  
    nextDirection = {  
        x: x,  
        y: y  
    };  
  
}  
  
  
/* =========================  
   MOVE  
========================= */  
  
function moveSnake() {  
  
    if (gameOver) {  
        return;  
    }  
  
    direction = nextDirection;  
  
    const head = {  
        x: snake[0].x + direction.x,  
        y: snake[0].y + direction.y  
    };  
  
  
    /* WALL = GAME OVER */  
  
    if (  
        head.x < 0 ||  
        head.x >= grid ||  
        head.y < 0 ||  
        head.y >= grid  
    ) {  
  
        gameOver = true;  
        return;  
  
    }  
  
  
    /*  
       IMPORTANT:  
       THERE IS NO BODY COLLISION CHECK.  
       THE SNAKE CAN TOUCH ITSELF.  
    */  
  
    snake.unshift(head);  
  
  
    /* FOOD */  
  
    if (  
        head.x === food.x &&  
        head.y === food.y  
    ) {  
  
        score++;  
  
        document.getElementById("score").textContent =  
            "🏆 Score: " + score;  
  
        createFood();  
  
    } else {  
  
        snake.pop();  
  
    }  
  
}  
  
  
/* =========================  
   DRAW GAME  
========================= */  
  
function draw() {  
  
    ctx.clearRect(  
        0,  
        0,  
        canvas.width,  
        canvas.height  
    );  
  
  
    /* FOOD */  
  
    ctx.font = "18px Arial";  
    ctx.textAlign = "center";  
    ctx.textBaseline = "middle";  
  
    ctx.fillText(  
        foodEmoji,  
        food.x * cell + 10,  
        food.y * cell + 10  
    );  
  
  
    /* SNAKE */  
  
    snake.forEach((part, index) => {  
  
        const x = part.x * cell + 10;  
        const y = part.y * cell + 10;  
  
  
        /* BODY */  
  
        if (index !== 0) {  
  
            ctx.fillStyle = snakeColor;  
  
            ctx.beginPath();  
  
            ctx.arc(  
                x,  
                y,  
                8,  
                0,  
                Math.PI * 2  
            );  
  
            ctx.fill();  
  
        }  
  
  
        /* HEAD */  
  
        else {  
  
            ctx.fillStyle = snakeColor;  
  
            ctx.beginPath();  
  
            ctx.arc(  
                x,  
                y,  
                9,  
                0,  
                Math.PI * 2  
            );  
  
            ctx.fill();  
  
  
            /* EYES */  
  
            ctx.fillStyle = "white";  
  
            let eye1X = x;  
            let eye1Y = y;  
  
            let eye2X = x;  
            let eye2Y = y;  
  
  
            if (direction.x === 1) {  
  
                eye1X += 4;  
                eye1Y -= 4;  
  
                eye2X += 4;  
                eye2Y += 4;  
  
            }  
  
            else if (direction.x === -1) {  
  
                eye1X -= 4;  
                eye1Y -= 4;  
  
                eye2X -= 4;  
                eye2Y += 4;  
  
            }  
  
            else if (direction.y === -1) {  
  
                eye1X -= 4;  
                eye1Y -= 4;  
  
                eye2X += 4;  
                eye2Y -= 4;  
  
            }  
  
            else {  
  
                eye1X -= 4;  
                eye1Y += 4;  
  
                eye2X += 4;  
                eye2Y += 4;  
  
            }  
  
  
            ctx.beginPath();  
  
            ctx.arc(  
                eye1X,  
                eye1Y,  
                3,  
                0,  
                Math.PI * 2  
            );  
  
            ctx.arc(  
                eye2X,  
                eye2Y,  
                3,  
                0,  
                Math.PI * 2  
            );  
  
            ctx.fill();  
  
  
            /* EYES */  
  
            ctx.fillStyle = "#222";  
  
            ctx.beginPath();  
  
            ctx.arc(  
                eye1X,  
                eye1Y,  
                1.5,  
                0,  
                Math.PI * 2  
            );  
  
            ctx.arc(  
                eye2X,  
                eye2Y,  
                1.5,  
                0,  
                Math.PI * 2  
            );  
  
            ctx.fill();  
  
        }  
  
    });  
  
  
    /* GAME OVER */  
  
    if (gameOver) {  
  
        ctx.fillStyle = "rgba(255,255,255,0.9)";  
  
        ctx.fillRect(  
            35,  
            130,  
            290,  
            100  
        );  
  
        ctx.fillStyle = "#b1124a";  
  
        ctx.font = "bold 30px Arial";  
  
        ctx.fillText(  
            "Game Over!",  
            180,  
            165  
        );  
  
        ctx.font = "18px Arial";  
  
        ctx.fillText(  
            "You hit the wall!",  
            180,  
            198  
        );  
  
    }  
  
}  
  
  
/* =========================  
   CONTROLS  
========================= */  
  
function addControl(id, x, y) {  
  
    document  
        .getElementById(id)  
        .addEventListener(  
            "pointerdown",  
            function(event) {  
  
                event.preventDefault();  
  
                changeDirection(x, y);  
  
            }  
        );  
  
}  
  
  
addControl("up", 0, -1);  
addControl("down", 0, 1);  
addControl("left", -1, 0);  
addControl("right", 1, 0);  
  
  
/* KEYBOARD */  
  
document.addEventListener(  
    "keydown",  
    function(event) {  
  
        if (  
            event.key === "ArrowUp" ||  
            event.key === "w"  
        ) {  
            changeDirection(0, -1);  
        }  
  
        if (  
            event.key === "ArrowDown" ||  
            event.key === "s"  
        ) {  
            changeDirection(0, 1);  
        }  
  
        if (  
            event.key === "ArrowLeft" ||  
            event.key === "a"  
        ) {  
            changeDirection(-1, 0);  
        }  
  
        if (  
            event.key === "ArrowRight" ||  
            event.key === "d"  
        ) {  
            changeDirection(1, 0);  
        }  
  
    }  
);  
  
  
/* =========================  
   SNAKE COLORS  
========================= */  
  
document  
    .querySelectorAll(  
        ".choice:not(.food)"  
    )  
    .forEach(  
        function(button) {  
  
            button.addEventListener(  
                "click",  
                function() {  
  
                    document  
                        .querySelectorAll(  
                            ".choice:not(.food)"  
                        )  
                        .forEach(  
                            b =>  
                            b.classList.remove(  
                                "selected"  
                            )  
                        );  
  
                    button.classList.add(  
                        "selected"  
                    );  
  
                    snakeColor =  
                        button.dataset.color;  
  
                    draw();  
  
                }  
            );  
  
        }  
    );  
  
  
/* =========================  
   FOOD CHOICES  
========================= */  
  
document  
    .querySelectorAll(".food")  
    .forEach(  
        function(button) {  
  
            button.addEventListener(  
                "click",  
                function() {  
  
                    document  
                        .querySelectorAll(  
                            ".food"  
                        )  
                        .forEach(  
                            b =>  
                            b.classList.remove(  
                                "selected"  
                            )  
                        );  
  
                    button.classList.add(  
                        "selected"  
                    );  
  
                    foodEmoji =  
                        button.dataset.food;  
  
                    draw();  
  
                }  
            );  
  
        }  
    );  
  
  
/* RESTART */  
  
document  
    .getElementById("restart")  
    .addEventListener(  
        "click",  
        restart  
    );  
  
  
/* START */  
  
restart();  
  
  
/* GAME SPEED */  
  
setInterval(  
    function() {  
  
        moveSnake();  
        draw();  
  
    },  
    115  
);  
  
</script>  </body>  
</html>  
""", height950)
