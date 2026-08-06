from flask import Flask, render_template_string, request, jsonify
import requests
import os

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = "8676717402:AAFt9CPRbzJPmhupqqJLs3J7Jqe_SnydU2E"
TELEGRAM_CHAT_ID = "-1003999368970"

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=yes">
    <title>Леонид & Алеся | Свадебное приглашение</title>
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Montserrat:wght@300;400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            background: #fef9f0;
            font-family: 'Montserrat', sans-serif;
            color: #2c3e2b;
            line-height: 1.5;
            overflow-x: hidden;
        }

        .section-dark {
            position: relative;
            background: #1a2e1f;
            color: white;
            padding: 140px 0;
            overflow: hidden;
        }

        .section-dark::before {
            content: "";
            position: absolute;
            top: -1px;
            left: 0;
            width: 100%;
            height: 120px;
            background: white;
            clip-path: polygon(
                0 35%, 8% 28%, 16% 40%, 24% 30%, 32% 48%, 40% 35%,
                48% 50%, 56% 32%, 64% 45%, 72% 30%, 80% 42%, 88% 25%,
                100% 36%, 100% 0, 0 0
            );
            z-index: 1;
        }

        .section-dark::after {
            content: "";
            position: absolute;
            bottom: -1px;
            left: 0;
            width: 100%;
            height: 120px;
            background: white;
            clip-path: polygon(
                0 100%, 0 65%, 8% 78%, 16% 60%, 24% 82%, 32% 62%,
                40% 76%, 48% 55%, 56% 72%, 64% 52%, 72% 68%,
                80% 48%, 88% 62%, 100% 40%, 100% 100%
            );
            z-index: 1;
        }

        .section-content {
            position: relative;
            z-index: 5;
        }

.garland {
    position: absolute;
    top: 25px;
    left: 0;
    width: 100%;
    height: 220px;
    pointer-events: none;
    z-index: 4;
}

.garland-bottom {
    top: auto;
    bottom: 25px;
    transform: rotateX(180deg);
}

.garland svg {
    width: 100%;
    height: 100%;
    display: block;
}

.garland path {
    stroke: rgba(255,255,255,0.25);
    stroke-width: 2;
    fill: none;
}

.garland circle {
    fill: #fff4b5;
    filter: drop-shadow(0 0 8px rgba(255,244,181,0.9));
    animation: glow 2s infinite alternate;
}

@keyframes glow {
    from { opacity: 0.5; }
    to { opacity: 1; }
}

/* Адаптация для мобильных устройств */
@media (max-width: 768px) {
    .section-dark {
        padding: 90px 0;
    }

    .garland {
        top: 15px;
        height: 90px;
    }

    .garland-bottom {
        top: auto;
        bottom: 15px;
    }

    .section-dark::before,
    .section-dark::after {
        height: 60px;
    }
}

@media (max-width: 480px) {
    .garland {
        top: 10px;
        height: 70px;
    }

    .garland-bottom {
        top: auto;
        bottom: 10px;
    }

    .section-dark {
        padding: 70px 0;
    }
}

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0;
        }

        .card {
            background: white;
            border-radius: 0;
            box-shadow: 0 1px 3px rgba(0,0,0,0.02);
            padding: 2rem 1.8rem;
            margin-bottom: 0;
            transition: none;
        }

        .section-dark .card {
            background: transparent;
            box-shadow: none;
        }

        .hero-start {
            background: white;
            border-radius: 0;
            padding: 2rem 1.5rem;
            margin-bottom: 0;
            text-align: center;
            box-shadow: none;
        }

        .photo-frame {
            width: 100%;
            aspect-ratio: 16 / 9;
            background: #ede5d8;
            border-radius: 32px;
            margin-bottom: 1.8rem;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            border: 1px solid #e0d5c5;
        }

        .photo-placeholder {
            max-width: 100%;
            max-height: 100%;
            width: auto;
            height: auto;
            object-fit: contain;
            display: block;
        }

        .date-large {
            font-family: 'Cormorant Garamond', serif;
            font-size: clamp(2.5rem, 12vw, 5rem);
            font-weight: 700;
            letter-spacing: 6px;
            color: #2b5e3b;
            margin: 0.5rem 0 0.2rem;
            text-align: center;
            background: white;
            padding: 1rem 0 0 0;
        }

        .names-large {
            font-family: 'Cormorant Garamond', serif;
            font-size: clamp(1.6rem, 7vw, 2.8rem);
            font-weight: 600;
            color: #2c3e2b;
            letter-spacing: 2px;
            margin: 0;
            border-top: 1px solid #cfe3cf;
            border-bottom: 1px solid #cfe3cf;
            padding: 0.6rem 1rem;
            text-align: center;
            background: white;
            width: 100%;
            display: block;
        }

        .invitation-text, .story-text {
            text-align: center;
            font-size: 1.2rem;
            line-height: 1.6;
            color: #2c3e2b;
            background: white;
            padding: 1.5rem 2rem;
        }

        .section-dark .story-text {
            background: transparent;
            color: white;
        }

        .invitation-text p, .story-text p {
            margin-bottom: 0.8rem;
        }

        .story-header {
            font-size: 1.8rem;
            font-family: 'Cormorant Garamond', serif;
            font-weight: 600;
            color: #2b5e3b;
            margin-bottom: 1rem;
        }

        .section-dark .story-header {
            color: #e6f0e3;
        }

        .couple-photos {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin: 1.5rem 0;
            flex-wrap: wrap;
        }

        .couple-photo {
            width: 250px;
            height: 250px;
            border-radius: 20px;
            overflow: hidden;
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        }

        .single-photo {
            width: 340px;
            height: 340px;
        }

        @media (max-width: 600px) {
            .single-photo {
                width: 240px;
                height: 240px;
            }
        }

        .couple-photo img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        @media (max-width: 600px) {
            .couple-photo {
                width: 180px;
                height: 180px;
            }
        }

        /* Контейнер для главного фото — квадратный и закруглённый */
        .main-photo-container {
            max-width: 300px;
            margin: 0 auto;
        }
        .main-photo-container img {
            width: 100%;
            aspect-ratio: 1 / 1;
            object-fit: cover;
            display: block;
            cursor: pointer;
            border-radius: 20px;
            box-shadow: none;
        }
        @media (max-width: 600px) {
            .main-photo-container {
                max-width: 200px;
            }
            .main-photo-container img {
                border-radius: 15px;
            }
        }

        /* Карусель */
        .carousel-container {
            position: relative;
            max-width: 800px;
            margin: 2rem auto;
            overflow: hidden;
            border-radius: 28px;
            box-shadow: 0 15px 30px rgba(0,0,0,0.1);
        }

        .carousel-slides {
            display: flex;
            transition: transform 0.5s ease;
        }

        .carousel-slide {
            min-width: 100%;
            aspect-ratio: 16 / 9;
            background: #ede5d8;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .carousel-slide img {
            width: 100%;
            height: 100%;
            object-fit: contain;
            display: block;
            cursor: pointer;
        }

        .carousel-btn {
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
            background: rgba(255,255,255,0.7);
            border: none;
            font-size: 2rem;
            cursor: pointer;
            padding: 0 1rem;
            border-radius: 50%;
            color: #2b5e3b;
            transition: 0.2s;
        }

        .carousel-btn:hover {
            background: white;
        }

        .prev {
            left: 10px;
        }

        .next {
            right: 10px;
        }

        .carousel-dots {
            text-align: center;
            margin-top: 0.5rem;
        }

        .dot {
            display: inline-block;
            width: 10px;
            height: 10px;
            border-radius: 50%;
            background: #ccc;
            margin: 0 5px;
            cursor: pointer;
        }

        .dot.active {
            background: #2b5e3b;
        }

        /* Лайтбокс для карусели */
        .lightbox {
            display: none;
            position: fixed;
            z-index: 10000;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.9);
            justify-content: center;
            align-items: center;
            flex-direction: column;
        }
        .lightbox.active {
            display: flex;
        }
        .lightbox-img {
            max-width: 90%;
            max-height: 80%;
            object-fit: contain;
            border-radius: 8px;
            box-shadow: 0 0 20px rgba(0,0,0,0.5);
        }
        .lightbox-controls {
            position: absolute;
            bottom: 20px;
            left: 0;
            right: 0;
            display: flex;
            justify-content: center;
            gap: 30px;
        }
        .lightbox-btn {
            background: rgba(255,255,255,0.2);
            border: none;
            font-size: 2rem;
            color: white;
            cursor: pointer;
            padding: 10px 20px;
            border-radius: 50%;
            transition: 0.3s;
        }
        .lightbox-btn:hover {
            background: rgba(255,255,255,0.5);
        }
        .lightbox-close {
            position: absolute;
            top: 20px;
            right: 30px;
            font-size: 2rem;
            color: white;
            cursor: pointer;
            background: none;
            border: none;
        }

        /* Отдельный лайтбокс для главного фото */
        .main-photo-lightbox {
            display: none;
            position: fixed;
            z-index: 10001;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.9);
            justify-content: center;
            align-items: center;
            cursor: pointer;
        }
        .main-photo-lightbox.active {
            display: flex;
        }
        .main-photo-lightbox-img {
            max-width: 90%;
            max-height: 90%;
            object-fit: contain;
            border-radius: 8px;
            box-shadow: 0 0 20px rgba(0,0,0,0.5);
        }
        .main-photo-close {
            position: absolute;
            top: 20px;
            right: 30px;
            font-size: 2rem;
            color: white;
            cursor: pointer;
            background: none;
            border: none;
            z-index: 10002;
        }

        .place-center { text-align: center; }
        .place-photo { width: 100%; aspect-ratio: 16/9; background: #ede5d8; border-radius: 32px; margin: 1rem 0; overflow: hidden; }
        .place-photo img { width: 100%; height: 100%; object-fit: cover; }
        .place-address { background: #ebf3e8; padding: 0.8rem 1.2rem; border-radius: 60px; display: inline-block; margin: 1rem auto; }
        .place-address a { color: #2b5e3b; text-decoration: none; font-weight: 500; }
        .instagram-link { display: inline-flex; align-items: center; gap: 0.5rem; background: #ebf3e8; padding: 0.5rem 1.2rem; border-radius: 60px; color: #2b5e3b; text-decoration: none; margin: 0.5rem auto; transition: background 0.2s; }
        .instagram-link:hover { background: #d4e2ce; }
        .map-container { margin-top: 1.5rem; border-radius: 32px; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.05); }
        .map-container iframe { width: 100%; height: 400px; border: 0; display: block; }

        h2 { font-size: 2rem; border-left: 5px solid #a3c9a3; padding-left: 1rem; margin-bottom: 1.5rem; color: #2c3e2b; font-family: 'Cormorant Garamond', serif; font-weight: 600; }
        .section-dark h2 { border-left-color: #f0f7ed; color: white; }

        .calendar { background: #fcf9f5; border-radius: 28px; padding: 1rem; text-align: center; }
        .calendar table { width: 100%; border-collapse: collapse; }
        .calendar th, .calendar td { padding: 0.7rem; text-align: center; font-size: 1rem; }
        .calendar .special-day {
            position: relative;
            width: 40px;
            height: 40px;
            margin: 0 auto;
            color: #2c3e2b;
            font-weight: bold;
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 1;
        }
        .calendar .special-day::before {
            content: "";
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -46%) rotate(-8deg);
            width: 48px;
            height: 48px;
            background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg width='24' height='24' viewBox='0 0 24 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3e%3cpath d='M12.3 20.1C7.8 16 4.6 11.7 5.1 7.6C5.4 4.5 8.3 3.2 11.1 6.3C12.4 7.7 12 7.7 13.1 6C14.7 3.6 18.5 3.3 19.8 6.8C21.1 10.3 16.9 15.6 11.3 21.2' stroke='%23709c74' stroke-width='1.2' stroke-linecap='round'/%3e%3c/svg%3e");
            background-size: contain;
            background-repeat: no-repeat;
            background-position: center;
            z-index: -1;
        }

        .timeline-item {
            display: flex;
            gap: 20px;
            margin-bottom: 1rem;
        }
        .timeline-time {
            font-weight: 700;
            min-width: 90px;
            color: #2b5e3b;
        }
        .section-dark .timeline-time {
            color: #e6f0e3;
        }
        .timeline-desc {
            flex: 1;
            font-size: 1rem;
            text-align: center;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .timeline-sub {
            display: block;
            font-size: 0.85rem;
            opacity: 0.8;
            font-style: italic;
            margin-top: 0.2rem;
            text-align: center;
        }
        @media (max-width: 700px) {
            .timeline-item {
                flex-direction: column;
                gap: 8px;
                text-align: center;
                align-items: center;
            }
            .timeline-time {
                min-width: auto;
                text-align: center;
            }
            .timeline-desc {
                text-align: center;
                align-items: center;
            }
        }

        .dress-row { display: flex; gap: 2rem; flex-wrap: wrap; justify-content: center; margin: 1.5rem 0; }
        .dress-col { flex: 1; min-width: 150px; text-align: center; background: #ebf3e8; padding: 1rem; border-radius: 28px; }
        .dress-col i { font-size: 2.5rem; color: #2b5e3b; }
        .countdown { display: flex; justify-content: space-between; gap: 1rem; flex-wrap: wrap; margin: 1.5rem 0; }
        .countdown-box { background: #ebf3e8; border-radius: 20px; padding: 1rem; flex: 1; text-align: center; min-width: 70px; }
        .countdown-number { font-size: 2.2rem; font-weight: 800; font-family: monospace; color: #2b5e3b; }
        .wishes-text { background: #f4f8f1; padding: 1.2rem; border-radius: 24px; margin: 1rem 0; }
        .wishes-text p { margin-bottom: 0.8rem; }
        .wishes-text p:last-child { margin-bottom: 0; }
        .btn { display: inline-block; background: #2b5e3b; color: white; border: none; padding: 12px 28px; border-radius: 50px; font-weight: 600; cursor: pointer; transition: 0.2s; text-decoration: none; margin: 0.5rem 0; }
        .btn-outline { background: transparent; border: 2px solid #2b5e3b; color: #2b5e3b; }
        .btn-outline:hover { background: #2b5e3b; color: white; }
        .contact-card { display: flex; align-items: center; gap: 1rem; background: #ebf3e8; padding: 1rem; border-radius: 50px; margin: 1rem 0; }
        .footer-note { text-align: center; margin-top: 0; font-size: 0.9rem; border-top: 1px solid #d9e8d4; padding: 2rem 1rem; background: white; color: #2b5e3b; }
        .signature { font-family: 'Cormorant Garamond', serif; font-size: 1.5rem; text-align: center; margin-top: 1rem; color: #2b5e3b; }
        i.fa, i.far { margin-right: 6px; }

        .dress-photos {
            display: flex;
            justify-content: center;
            gap: 15px;
            flex-wrap: wrap;
            margin: 1rem 0;
        }
        .dress-photo {
            width: 100px;
            height: 130px;
            object-fit: cover;
            border-radius: 16px;
            box-shadow: 0 6px 12px rgba(0,0,0,0.1);
            transition: transform 0.2s;
        }
        .dress-photo:hover {
            transform: scale(1.05);
        }
        @media (max-width: 700px) {
            .dress-photo { width: 80px; height: 105px; }
        }
        @media (max-width: 550px) {
            .dress-photo { width: 70px; height: 90px; }
        }

        .video-placeholder {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        .form-group {
            margin-bottom: 1.5rem;
        }
        .form-group label {
            display: block;
            font-weight: 600;
            margin-bottom: 0.5rem;
            font-size: 0.9rem;
            letter-spacing: 1px;
            color: #2c3e2b;
        }
        .form-input {
            width: 100%;
            padding: 12px 15px;
            border: 1px solid #dbebd4;
            border-radius: 50px;
            background: #fefaf5;
            font-family: 'Montserrat', sans-serif;
            font-size: 1rem;
            transition: 0.2s;
        }
        .form-input:focus {
            outline: none;
            border-color: #2b5e3b;
            box-shadow: 0 0 0 3px rgba(43,94,59,0.1);
        }
        .radio-group, .checkbox-group {
            display: flex;
            flex-wrap: wrap;
            gap: 1rem;
            justify-content: center;
        }
        .radio-label, .checkbox-label {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            cursor: pointer;
            background: #ebf3e8;
            padding: 0.4rem 1rem;
            border-radius: 60px;
            font-size: 0.9rem;
            color: #2c3e2b;
        }
        .radio-label input, .checkbox-label input {
            margin: 0;
            transform: scale(1.1);
        }
        @media (max-width: 600px) {
            .radio-group, .checkbox-group { gap: 0.7rem; }
            .radio-label, .checkbox-label { padding: 0.3rem 0.8rem; font-size: 0.8rem; }
        }
        .photo-full {
            width: 100%;
            background: #ede5d8;
            border-radius: 32px;
            padding: 0;
        }
        .photo-full img {
            width: 100%;
            height: auto;
            display: block;
            border-radius: 32px;
        }
        .toast-notification {
            position: fixed;
            bottom: 30px;
            left: 50%;
            transform: translateX(-50%) translateY(100px);
            background: #2b5e3b;
            color: white;
            padding: 12px 24px;
            border-radius: 50px;
            font-size: 1rem;
            font-weight: 500;
            z-index: 1000;
            opacity: 0;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            display: flex;
            align-items: center;
            gap: 10px;
            pointer-events: none;
        }
        .toast-notification.show {
            opacity: 1;
            transform: translateX(-50%) translateY(0);
        }
        .toast-notification i { font-size: 1.2rem; }
        .overnight-count {
            display: none;
            margin-top: 0.5rem;
        }

        .countdown-box {
            background: #ebf3e8;
            border-radius: 20px;
            padding: 1rem;
            flex: 1;
            text-align: center;
            min-width: 70px;
        }
        .countdown-number {
            font-size: 2.2rem;
            font-weight: 800;
            font-family: monospace;
            color: #2b5e3b;
            display: inline-block;
            min-width: 60px;
            text-align: center;
        }
        @media (max-width: 700px) {
            .countdown-number {
                font-size: 1.8rem;
                min-width: 50px;
            }
            .countdown-box {
                padding: 0.8rem;
                min-width: 60px;
            }
        }
        @media (max-width: 550px) {
            .countdown-number {
                font-size: 1.4rem;
                min-width: 42px;
            }
            .countdown-box {
                padding: 0.5rem;
                min-width: 50px;
            }
        }

        .dress-rules {
            display: flex;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 20px;
            font-size: 18px;
        }
        .rule-left, .rule-right {
            flex: 1;
            text-align: left;
            background: #f9f9f9;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        }
        @media (max-width: 768px) {
            .dress-rules {
                flex-direction: column;
            }
        }
        .rule-left::before, .rule-right::before {
            content: "◆";
            color: #2b5e3b;
            font-weight: bold;
            margin-right: 8px;
            font-size: 1.1em;
            display: inline-block;
        }
    </style>
</head>
<body>

<div class="container">
    <div class="date-large">04 · 09 · 26</div>
    <div class="names-large">ЛЕОНИД & АЛЕСЯ</div>

    <div class="hero-start">
        <div class="photo-frame">
            <video class="video-placeholder" autoplay muted loop playsinline>
                <source src="static/images/video.mp4" type="video/mp4">
                Ваш браузер не поддерживает видео.
            </video>
        </div>
    </div>

    <div class="invitation-text">
        <p><strong>Дорогие друзья!</strong></p>
        <p>Это официальное приглашение на нашу свадьбу! А получили вы его потому, что мы очень хотим видеть вас в этот день рядом с нами!</p>
    </div>

    <section class="section-dark">
        <div class="garland">
            <svg viewBox="0 0 1440 320" preserveAspectRatio="none">
                <path d="M0,80 C200,180 400,20 720,120 C980,200 1200,40 1440,120"></path>
                <circle cx="80" cy="100" r="5"/>
                <circle cx="180" cy="130" r="5"/>
                <circle cx="280" cy="90" r="5"/>
                <circle cx="380" cy="140" r="5"/>
                <circle cx="480" cy="100" r="5"/>
                <circle cx="580" cy="150" r="5"/>
                <circle cx="680" cy="110" r="5"/>
                <circle cx="780" cy="145" r="5"/>
                <circle cx="880" cy="100" r="5"/>
                <circle cx="980" cy="140" r="5"/>
                <circle cx="1080" cy="90" r="5"/>
                <circle cx="1180" cy="135" r="5"/>
                <circle cx="1280" cy="95" r="5"/>
            </svg>
        </div>
        <div class="section-content">
            <div class="card" style="text-align:center">
                <div class="story-header">✨ Немного о нас ✨</div>
                <p style="font-size:1.2rem">Он и она — две разные истории, которые решили стать одной.</p>
                <div class="couple-photos">
                    <div class="main-photo-container">
                        <img src="/static/images/Детская.png" alt="Леонид и Алеся" id="mainWeddingPhoto" onerror="this.src='https://placehold.co/800x800?text=Фото'">
                    </div>
                </div>
                <div class="story-text">
                    <p><strong>Дорогие родные и друзья!</strong></p>
                    <p>Жить, любить, расти — вот что важно для нас. И мы решили, что по жизни будем идти только вместе. С радостью приглашаем вас на наш свадебный праздник. Будем счастливы разделить этот день с вами!</p>
                </div>
                <div class="carousel-container">
                    <div class="carousel-slides" id="carouselSlides">
                        <div class="carousel-slide"><img src="static/images/photo_2026-05-12_15-48-19.jpg" alt="Фото 1"></div>
                        <div class="carousel-slide"><img src="static/images/photo_2026-05-12_15-48-01.jpg" alt="Фото 2"></div>
                        <div class="carousel-slide"><img src="static/images/photo_2026-05-12_15-47-57.jpg" alt="Фото 3"></div>
                        <div class="carousel-slide"><img src="static/images/photo_2026-05-12_15-48-53.jpg" alt="Фото 4"></div>
                        <div class="carousel-slide"><img src="static/images/photo_2026-05-12_15-48-58.jpg" alt="Фото 5"></div>
                        <div class="carousel-slide"><img src="static/images/photo_2026-05-12_15-49-06.jpg" alt="Фото 6"></div>
                        <div class="carousel-slide"><img src="static/images/photo_2026-05-12_15-48-15.jpg" alt="Фото 7"></div>
                        <div class="carousel-slide"><img src="static/images/photo_2026-05-12_15-47-51.jpg" alt="Фото 8"></div>
                        <div class="carousel-slide"><img src="static/images/photo_2026-05-12_15-48-28.jpg" alt="Фото 9"></div>
                        <div class="carousel-slide"><img src="static/images/photo_2026-05-12_15-49-02.jpg" alt="Фото 10"></div>
                        <div class="carousel-slide"><img src="static/images/image_2026-05-19_20-23-30.png" alt="Фото 11"></div>
                        <div class="carousel-slide"><img src="static/images/photo_2026-05-19_20-09-51.jpg" alt="Фото 12"></div>
                        <div class="carousel-slide"><img src="static/images/IMG_1274 (1).jpg" alt="Фото 13"></div>
                    </div>
                    <button class="carousel-btn prev" id="prevBtn">❮</button>
                    <button class="carousel-btn next" id="nextBtn">❯</button>
                    <div class="carousel-dots" id="carouselDots"></div>
                </div>
            </div>
        </div>
        <div class="garland garland-bottom">
            <svg viewBox="0 0 1440 320" preserveAspectRatio="none">
                <path d="M0,80 C200,180 400,20 720,120 C980,200 1200,40 1440,120"></path>
                <circle cx="80" cy="100" r="5"/>
                <circle cx="180" cy="130" r="5"/>
                <circle cx="280" cy="90" r="5"/>
                <circle cx="380" cy="140" r="5"/>
                <circle cx="480" cy="100" r="5"/>
                <circle cx="580" cy="150" r="5"/>
                <circle cx="680" cy="110" r="5"/>
                <circle cx="780" cy="145" r="5"/>
                <circle cx="880" cy="100" r="5"/>
                <circle cx="980" cy="140" r="5"/>
                <circle cx="1080" cy="90" r="5"/>
                <circle cx="1180" cy="135" r="5"/>
                <circle cx="1280" cy="95" r="5"/>
            </svg>
        </div>
    </section>

    <div class="card">
    <h2><i class="far fa-calendar-alt"></i> СЕНТЯБРЬ 2026</h2>
    <div class="calendar">
        <div class="month-name">СЕНТЯБРЬ</div>
        <table>
            <thead><tr><th>ПН</th><th>ВТ</th><th>СР</th><th>ЧТ</th><th>ПТ</th><th>СБ</th><th>ВС</th></tr></thead>
            <tbody>
                <tr><td style="opacity:0"> </td><td>1</td><td>2</td><td>3</td><td class="special-day">4</td><td>5</td><td>6</td></tr>
                <tr><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td></tr>
                <tr><td>14</td><td>15</td><td>16</td><td>17</td><td>18</td><td>19</td><td>20</td></tr>
                <tr><td>21</td><td>22</td><td>23</td><td>24</td><td>25</td><td>26</td><td>27</td></tr>
                <tr><td>28</td><td>29</td><td>30</td><td style="opacity:0"> </td><td style="opacity:0"> </td><td style="opacity:0"> </td><td style="opacity:0"> </td></tr>
            </tbody>
        </table>
        <p><i class="fas fa-heart" style="color:#2b5e3b;"></i> День свадьбы – 4 СЕНТЯБРЯ</p>
    </div>
</div>

    <div class="card place-center">
        <h2><i class="fas fa-map-marker-alt"></i> МЕСТО ПРОВЕДЕНИЯ</h2>
        <p>Наша свадьба пройдёт в <strong>Усадебно-парковом комплексе Радзивилки</strong>. Это восстановленная усадьба 19 века, расположенная в 30 километрах от Гродно.</p>
        <a href="https://www.instagram.com/radzivilki/" class="instagram-link" target="_blank" rel="noopener noreferrer"><i class="fab fa-instagram"></i> Смотреть в Instagram</a>
        <div class="place-photo"><img src="static/images/Усадьба.jpg" alt="Усадьба" onerror="this.src='https://placehold.co/800x450?text=Фото+усадьбы'"></div>
        <div class="place-address"><i class="fas fa-location-dot"></i> <a href="https://yandex.by/maps/?text=Гродненский+район,+Сопоцкинский+сельсовет,+деревня+Радзивилки,+44" target="_blank">Гродненский район, Сопоцкинский сельсовет, деревня Радзивилки, 44</a></div>
        <div class="map-container"><iframe src="https://yandex.ru/map-widget/v1/?um=constructor%3A1a2b3c4d5e6f7g8h9i0j&amp;source=constructor&amp;mode=search&amp;text=Усадебно-парковый комплекс Радзивилки, деревня Радзивилки, 44&amp;z=17" allowfullscreen="true"></iframe></div>
    </div>

    <section class="section-dark">
        <div class="garland">
            <svg viewBox="0 0 1440 320" preserveAspectRatio="none">
                <path d="M0,80 C200,180 400,20 720,120 C980,200 1200,40 1440,120"></path>
                <circle cx="100" cy="100" r="5"/>
                <circle cx="250" cy="140" r="5"/>
                <circle cx="400" cy="100" r="5"/>
                <circle cx="550" cy="145" r="5"/>
                <circle cx="700" cy="110" r="5"/>
                <circle cx="850" cy="140" r="5"/>
                <circle cx="1000" cy="100" r="5"/>
                <circle cx="1150" cy="140" r="5"/>
                <circle cx="1300" cy="95" r="5"/>
            </svg>
        </div>
        <div class="section-content">
            <div class="card">
                <h2><i class="far fa-calendar-alt"></i> ПРОГРАММА СВАДЬБЫ</h2>
                <div class="program-day">
                    <h3 style="font-size:1.5rem; margin-bottom:1rem;">04 сентября 2026</h3>
                    <div class="timeline-item"><span class="timeline-time">13:00</span><span class="timeline-desc">Трансфер из Гродно</span></div>
                    <div class="timeline-item"><span class="timeline-time">14:00</span><span class="timeline-desc">Сбор гостей / welcome-зона<br><span class="timeline-sub">Заселение в гостиницу</span></span></div>
                    <div class="timeline-item"><span class="timeline-time">15:00</span><span class="timeline-desc">Фуршет и приветственные напитки<br><span class="timeline-sub">Освежающие коктейли и закуски, пока все собираются.</span></span></div>
                    <div class="timeline-item"><span class="timeline-time">16:00</span><span class="timeline-desc">Церемония бракосочетания<br><span class="timeline-sub">Самое трогательное — соединение двух сердец перед родными и друзьями.</span></span></div>
                    <div class="timeline-item"><span class="timeline-time">16:30</span><span class="timeline-desc">Фотосессия с гостями и семьёй<br><span class="timeline-sub">Запечатлеваем радость — общие фото на память с самыми близкими.</span></span></div>
                    <div class="timeline-item"><span class="timeline-time">17:00</span><span class="timeline-desc">Начало банкета</span></div>
                    <div class="timeline-item"><span class="timeline-time">23:00</span><span class="timeline-desc">Финальный аккорд вечера<br></span></div>
                </div>
                <div class="program-day">
                    <h3 style="font-size:1.5rem; margin:1.5rem 0 1rem;">05 сентября 2026</h3>
                    <div class="timeline-item"><span class="timeline-time">01:00</span><span class="timeline-desc">Окончание торжества</span></div>
                    <div class="timeline-item"><span class="timeline-time">09:00</span><span class="timeline-desc">Завтрак<br><span class="timeline-sub">Завтрак будет длиться до 11:00</span></span></div>
                    <div class="timeline-item"><span class="timeline-time">12:00</span><span class="timeline-desc">Выселение, отъезд<br><span class="timeline-sub">Прощание с гостями</span></span></div>
                    <div class="timeline-item"><span class="timeline-time">12:30</span><span class="timeline-desc">Второй день свадьбы(Усадьба Соничи)<br><span class="timeline-sub">Переезд в новое место для продолжения торжества в неформальной обстановке. Задача: прихватить удобную одежду, обувь, купальные костюмы.</span></span></div>
                </div>
            </div>
        </div>
        <div class="garland garland-bottom">
            <svg viewBox="0 0 1440 320" preserveAspectRatio="none">
                <path d="M0,80 C200,180 400,20 720,120 C980,200 1200,40 1440,120"></path>
                <circle cx="100" cy="100" r="5"/>
                <circle cx="250" cy="140" r="5"/>
                <circle cx="400" cy="100" r="5"/>
                <circle cx="550" cy="145" r="5"/>
                <circle cx="700" cy="110" r="5"/>
                <circle cx="850" cy="140" r="5"/>
                <circle cx="1000" cy="100" r="5"/>
                <circle cx="1150" cy="140" r="5"/>
                <circle cx="1300" cy="95" r="5"/>
            </svg>
        </div>
    </section>

    <div class="card">
        <h2><i class="fas fa-tshirt"></i> ДРЕСС-КОД</h2>
        <p style="text-align: center; font-size: 22px; font-weight: bold; margin-bottom: 30px;">
            Будем рады, если вы подойдёте к выбору наряда<br>
            с соблюдением следующих правил дресс-кода:
        </p>
        <div class="dress-rules">
            <div class="rule-left">Для девушек – просим воздержаться от красных и белых нарядов.</div>
            <div class="rule-right">Для мужчин – вечерний костюм, пиджак с брюками или рубашка с брюками.</div>
        </div>
    </div>

    <div class="card">
        <h2><i class="fas fa-hourglass-half"></i> ДО СВАДЬБЫ ОСТАЛОСЬ</h2>
        <div class="countdown" id="countdown">
            <div class="countdown-box"><div class="countdown-number" id="days">00</div><div>дней</div></div>
            <div class="countdown-box"><div class="countdown-number" id="hours">00</div><div>часов</div></div>
            <div class="countdown-box"><div class="countdown-number" id="minutes">00</div><div>минут</div></div>
            <div class="countdown-box"><div class="countdown-number" id="seconds">00</div><div>секунд</div></div>
        </div>
        <div class="wishes-text">
            <p><strong>Пожелания:</strong></p>
            <p><i class="fas fa-kiss-wink-heart"></i> Будем очень признательны, если Вы воздержитесь от криков «Горько». Ведь поцелуй – это знак выражения чувств, и он не может быть по заказу. Однако, за сказанный тост мы с удовольствием вас порадуем :)</p>
            <p>🥂 Мы будем очень рады, если вместо цветочных букетов вы пополните наш домашний бар вашей любимой бутылочкой.</p>
        </div>
    </div>

    <div class="card">
        <h2><i class="fas fa-phone-alt"></i> КОНТАКТЫ</h2>
        <p>По всем вопросам, связанным с мероприятием, вы можете обратиться к нам.</p>
        <div class="contact-card"><i class="fas fa-user-circle" style="font-size:2rem"></i><div><strong>Леонид</strong><br>+375 (29) 595-60-35</div><i class="fas fa-candle" style="margin-left:auto; font-size:1.6rem"></i></div>
        <div class="contact-card"><i class="fas fa-user-circle" style="font-size:2rem"></i><div><strong>Алеся</strong><br>+375 (29) 201-05-55</div><i class="fas fa-candle" style="margin-left:auto; font-size:1.6rem"></i></div>
        <div class="contact-card"><i class="fab fa-telegram-plane" style="font-size:2rem"></i><div><strong>Вся актуальная информация будет публиковаться в Telegram-группе</strong><br><a href="https://t.me/+O4kiLkdTvKtmMTEy" target="_blank" style="color:#2b5e3b;">Присоединиться</a></div><i class="fas fa-candle" style="margin-left:auto; font-size:1.6rem"></i></div>
    </div>

    <div class="card" style="text-align:center">
        <h2 style="text-align:center">АНКЕТА ГОСТЯ</h2>
        <p>Пожалуйста, подтвердите ваше присутствие на нашей свадьбе до<br><strong>4 АВГУСТА 2026</strong></p>
        <form id="guestForm" style="max-width:600px; margin:0 auto">
            <div class="form-group"><label>ВАШЕ ИМЯ И ФАМИЛИЯ</label><input type="text" id="guestName" placeholder="Имя и Фамилия" required class="form-input"></div>
            <div class="form-group"><label>ПЛАНИРУЕТЕ ЛИ ВЫ ПРИСУТСТВОВАТЬ?</label><div class="radio-group"><label class="radio-label"><input type="radio" name="attendance" value="yes" required> С удовольствием приду!</label><label class="radio-label"><input type="radio" name="attendance" value="no" required> К сожалению, не смогу</label></div></div>
            <div id="extraFields">
                <!-- Алкоголь для гостя -->
                <div class="form-group"><label>ВАШИ ПРЕДПОЧТЕНИЯ (алкоголь)</label><div class="checkbox-group" id="guestDrinksGroup">
                    <label class="checkbox-label"><input type="checkbox" name="drinks" value="Шампанское"> Шампанское</label>
                    <label class="checkbox-label"><input type="checkbox" name="drinks" value="Белое вино"> Белое вино</label>
                    <label class="checkbox-label"><input type="checkbox" name="drinks" value="Красное вино"> Красное вино</label>
                    <label class="checkbox-label"><input type="checkbox" value="Виски"> Виски</label>
                    <label class="checkbox-label"><input type="checkbox" value="Водка"> Водка</label>
                    <label class="checkbox-label"><input type="checkbox" value="Джин"> Джин</label>
                    <label class="checkbox-label"><input type="checkbox" value="Ром"> Ром</label>
                    <label class="checkbox-label"><input type="checkbox" value="Не пью алкоголь"> Не пью алкоголь</label>
                </div></div>

                <!-- Поле для спутника -->
                <div class="form-group"><label>Если вы будете не один, заполните поле ниже</label><input type="text" id="companionName" placeholder="Имя и фамилия вашего спутника/спутницы" class="form-input"></div>

                <!-- Блок алкоголя для спутника (скрыт, появляется при вводе имени) -->
                <div id="companionAlcoholBlock" style="display: none;">
                    <div class="form-group"><label>ПРЕДПОЧТЕНИЯ СПУТНИКА (алкоголь)</label><div class="checkbox-group" id="companionDrinksGroup">
                        <label class="checkbox-label"><input type="checkbox" name="companionDrinks" value="Шампанское"> Шампанское</label>
                        <label class="checkbox-label"><input type="checkbox" name="companionDrinks" value="Белое вино"> Белое вино</label>
                        <label class="checkbox-label"><input type="checkbox" name="companionDrinks" value="Красное вино"> Красное вино</label>
                        <label class="checkbox-label"><input type="checkbox" name="companionDrinks" value="Виски"> Виски</label>
                        <label class="checkbox-label"><input type="checkbox" name="companionDrinks" value="Водка"> Водка</label>
                        <label class="checkbox-label"><input type="checkbox" name="companionDrinks" value="Джин"> Джин</label>
                        <label class="checkbox-label"><input type="checkbox" name="companionDrinks" value="Ром"> Ром</label>
                        <label class="checkbox-label"><input type="checkbox" name="companionDrinks" value="Не пью алкоголь"> Не пью алкоголь</label>
                    </div></div>
                </div>

                <div class="form-group"><label>Понадобится ли вам трансфер до или после мероприятия?</label><div class="checkbox-group">
                    <label class="checkbox-label"><input type="checkbox" name="transfer" value="До мероприятия"> До мероприятия</label>
                    <label class="checkbox-label"><input type="checkbox" name="transfer" value="После мероприятия"> После мероприятия</label>
                    <label class="checkbox-label"><input type="checkbox" name="transfer" value="Нет"> Нет</label>
                </div></div>
                <div class="form-group">
                    <label>Планируете ли вы остаться с ночёвкой?</label>
                    <div class="radio-group">
                        <label class="radio-label"><input type="radio" name="overnightYes" value="Да"> Да</label>
                        <label class="radio-label"><input type="radio" name="overnightYes" value="Нет"> Нет</label>
                    </div>
                    <div id="overnightCountGroup" class="overnight-count">
                        <input type="text" id="overnightCount" class="form-input" placeholder="Сколько человек?">
                    </div>
                </div>
                <div class="form-group"><label>Второй день мы будем праздновать в усадьбе неподалёку от Радзивилок. Вы с нами?</label>
                    <div class="radio-group">
                        <label class="radio-label"><input type="radio" name="secondDay" value="Да"> Да</label>
                        <label class="radio-label"><input type="radio" name="secondDay" value="Нет"> Нет</label>
                    </div>
                </div>
                <!-- НОВЫЙ БЛОК: ночёвка на второй день (появляется при ответе "Да" на второй день) -->
                <div id="secondDayOvernightBlock" style="display: none;">
                    <div class="form-group">
                        <label>Планируете ли вы остаться с ночёвкой на второй день?</label>
                        <div class="radio-group">
                            <label class="radio-label"><input type="radio" name="secondDayOvernight" value="Да"> Да</label>
                            <label class="radio-label"><input type="radio" name="secondDayOvernight" value="Нет"> Нет</label>
                        </div>
                    </div>
                </div>
            </div>
            <button type="submit" class="btn btn-outline"><i class="fas fa-check-circle"></i> ОТПРАВИТЬ</button>
            <div id="formResultMsg" style="margin-top:15px; font-size:0.9rem; text-align:center"></div>
        </form>
    </div>

    <div class="card" style="text-align:center"><div class="photo-full"><img src="static/images/0e4f5960-4617-4b39-bc4c-d97f98c20546.png" alt="Фото на память" onerror="this.src='https://placehold.co/800x450?text=Ваше+фото'"></div></div>

    <div class="card" style="text-align:center"><p><i class="fas fa-leaf"></i> До скорой встречи! <br> С любовью</p><div class="signature">ЛЕОНИД & АЛЕСЯ</div></div>
    <div class="footer-note"><i class="fas fa-heart"></i> Ждём вас на нашей свадьбе!</div>
</div>

<!-- Лайтбокс для карусели -->
<div id="lightbox" class="lightbox">
    <button class="lightbox-close">&times;</button>
    <img id="lightboxImg" class="lightbox-img" src="" alt="Увеличенное фото">
    <div class="lightbox-controls">
        <button class="lightbox-btn" id="prevLightbox">❮</button>
        <button class="lightbox-btn" id="nextLightbox">❯</button>
    </div>
</div>

<!-- Отдельный лайтбокс для главного фото -->
<div id="mainPhotoLightbox" class="main-photo-lightbox">
    <span class="main-photo-close">&times;</span>
    <img class="main-photo-lightbox-img" id="mainPhotoLightboxImg" src="" alt="Увеличенное фото">
</div>

<script>
    // Таймер
    const weddingDate = new Date(2026, 8, 4, 13, 0, 0).getTime();
    function updateCountdown() {
        const now = new Date().getTime();
        const distance = weddingDate - now;
        if (distance < 0) {
            document.getElementById('days').innerText = '0';
            document.getElementById('hours').innerText = '0';
            document.getElementById('minutes').innerText = '0';
            document.getElementById('seconds').innerText = '0';
            return;
        }
        const days = Math.floor(distance / (1000*60*60*24));
        const hours = Math.floor((distance % (24*60*60*1000)) / (1000*60*60));
        const minutes = Math.floor((distance % (60*60*1000)) / (1000*60));
        const seconds = Math.floor((distance % (60*1000)) / 1000);
        document.getElementById('days').innerText = days < 10 ? '0'+days : days;
        document.getElementById('hours').innerText = hours < 10 ? '0'+hours : hours;
        document.getElementById('minutes').innerText = minutes < 10 ? '0'+minutes : minutes;
        document.getElementById('seconds').innerText = seconds < 10 ? '0'+seconds : seconds;
    }
    updateCountdown();
    setInterval(updateCountdown, 1000);

    // Карусель
    const slides = document.querySelector('.carousel-slides');
    const slideItems = document.querySelectorAll('.carousel-slide');
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const dotsContainer = document.getElementById('carouselDots');
    if (slides && slideItems.length > 0) {
        let currentIndex = 0;
        let totalSlides = slideItems.length;
        function updateCarousel() {
            slides.style.transform = `translateX(-${currentIndex * 100}%)`;
            document.querySelectorAll('.dot').forEach((dot, idx) => {
                dot.classList.toggle('active', idx === currentIndex);
            });
        }
        function createDots() {
            dotsContainer.innerHTML = '';
            for (let i = 0; i < totalSlides; i++) {
                const dot = document.createElement('span');
                dot.classList.add('dot');
                if (i === currentIndex) dot.classList.add('active');
                dot.addEventListener('click', () => { currentIndex = i; updateCarousel(); });
                dotsContainer.appendChild(dot);
            }
        }
        createDots();
        prevBtn.addEventListener('click', () => { currentIndex = (currentIndex - 1 + totalSlides) % totalSlides; updateCarousel(); });
        nextBtn.addEventListener('click', () => { currentIndex = (currentIndex + 1) % totalSlides; updateCarousel(); });
    }

    // Лайтбокс для карусели
    const carouselImages = document.querySelectorAll('.carousel-slide img');
    const lightbox = document.getElementById('lightbox');
    const lightboxImg = document.getElementById('lightboxImg');
    const closeLightboxBtn = document.querySelector('.lightbox-close');
    const prevLightbox = document.getElementById('prevLightbox');
    const nextLightbox = document.getElementById('nextLightbox');
    let currentImageIndex = 0;

    function openLightbox(index) {
        if (!carouselImages.length) return;
        currentImageIndex = index;
        lightboxImg.src = carouselImages[currentImageIndex].src;
        lightbox.classList.add('active');
        document.body.style.overflow = 'hidden';
    }

    function closeLightbox() {
        lightbox.classList.remove('active');
        document.body.style.overflow = '';
    }

    function nextImage() {
        currentImageIndex = (currentImageIndex + 1) % carouselImages.length;
        lightboxImg.src = carouselImages[currentImageIndex].src;
    }

    function prevImage() {
        currentImageIndex = (currentImageIndex - 1 + carouselImages.length) % carouselImages.length;
        lightboxImg.src = carouselImages[currentImageIndex].src;
    }

    carouselImages.forEach((img, idx) => {
        img.addEventListener('click', (e) => {
            e.stopPropagation();
            openLightbox(idx);
        });
    });

    closeLightboxBtn.addEventListener('click', closeLightbox);
    prevLightbox.addEventListener('click', prevImage);
    nextLightbox.addEventListener('click', nextImage);
    lightbox.addEventListener('click', (e) => {
        if (e.target === lightbox) closeLightbox();
    });
    document.addEventListener('keydown', (e) => {
        if (!lightbox.classList.contains('active')) return;
        if (e.key === 'ArrowLeft') prevImage();
        else if (e.key === 'ArrowRight') nextImage();
        else if (e.key === 'Escape') closeLightbox();
    });

    // Отдельный лайтбокс для главного фото
    const mainPhoto = document.getElementById('mainWeddingPhoto');
    const mainLightbox = document.getElementById('mainPhotoLightbox');
    const mainLightboxImg = document.getElementById('mainPhotoLightboxImg');
    const mainClose = document.querySelector('.main-photo-close');

    if (mainPhoto && mainLightbox) {
        mainPhoto.addEventListener('click', (e) => {
            e.stopPropagation();
            mainLightboxImg.src = mainPhoto.src;
            mainLightbox.classList.add('active');
            document.body.style.overflow = 'hidden';
        });
        if (mainClose) {
            mainClose.addEventListener('click', () => {
                mainLightbox.classList.remove('active');
                document.body.style.overflow = '';
            });
        }
        mainLightbox.addEventListener('click', (e) => {
            if (e.target === mainLightbox) {
                mainLightbox.classList.remove('active');
                document.body.style.overflow = '';
            }
        });
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && mainLightbox.classList.contains('active')) {
                mainLightbox.classList.remove('active');
                document.body.style.overflow = '';
            }
        });
    }

    // Показ/скрытие полей при выборе "не смогу"
    const extraFields = document.getElementById('extraFields');
    const attendanceRadios = document.querySelectorAll('input[name="attendance"]');
    function toggleExtraFields() {
        const selected = document.querySelector('input[name="attendance"]:checked');
        if (selected && selected.value === 'no') {
            extraFields.style.display = 'none';
        } else {
            extraFields.style.display = 'block';
        }
    }
    attendanceRadios.forEach(radio => radio.addEventListener('change', toggleExtraFields));
    toggleExtraFields();

    // Показ/скрытие поля "Сколько человек?" при выборе "Да" для ночёвки
    const overnightYesRadios = document.querySelectorAll('input[name="overnightYes"]');
    const overnightCountGroup = document.getElementById('overnightCountGroup');
    function toggleOvernightCount() {
        const selected = document.querySelector('input[name="overnightYes"]:checked');
        if (selected && selected.value === 'Да') {
            overnightCountGroup.style.display = 'block';
        } else {
            overnightCountGroup.style.display = 'none';
            document.getElementById('overnightCount').value = '';
        }
    }
    overnightYesRadios.forEach(radio => radio.addEventListener('change', toggleOvernightCount));
    toggleOvernightCount();

    // НОВАЯ ФУНКЦИЯ: показ/скрытие вопроса о ночёвке на второй день
    const secondDayRadios = document.querySelectorAll('input[name="secondDay"]');
    const secondDayOvernightBlock = document.getElementById('secondDayOvernightBlock');
    function toggleSecondDayOvernight() {
        const selected = document.querySelector('input[name="secondDay"]:checked');
        if (selected && selected.value === 'Да') {
            secondDayOvernightBlock.style.display = 'block';
        } else {
            secondDayOvernightBlock.style.display = 'none';
            document.querySelectorAll('input[name="secondDayOvernight"]').forEach(radio => radio.checked = false);
        }
    }
    secondDayRadios.forEach(radio => radio.addEventListener('change', toggleSecondDayOvernight));
    toggleSecondDayOvernight();

    // НОВАЯ ФУНКЦИЯ: показ/скрытие блока алкоголя для спутника при вводе текста
    const companionNameInput = document.getElementById('companionName');
    const companionAlcoholBlock = document.getElementById('companionAlcoholBlock');
    function toggleCompanionAlcohol() {
        if (companionNameInput.value.trim() !== '') {
            companionAlcoholBlock.style.display = 'block';
        } else {
            companionAlcoholBlock.style.display = 'none';
            document.querySelectorAll('input[name="companionDrinks"]').forEach(cb => cb.checked = false);
        }
    }
    if (companionNameInput) {
        companionNameInput.addEventListener('input', toggleCompanionAlcohol);
        toggleCompanionAlcohol();
    }

    // Функция показа тоста
    function showToast(message, isError = false) {
        let toast = document.getElementById('toastMsg');
        if (!toast) {
            toast = document.createElement('div');
            toast.id = 'toastMsg';
            toast.className = 'toast-notification';
            document.body.appendChild(toast);
        }
        toast.innerHTML = `<i class="fas ${isError ? 'fa-exclamation-triangle' : 'fa-check-circle'}"></i> ${message}`;
        toast.style.background = isError ? '#c95a5a' : '#2b5e3b';
        toast.classList.add('show');
        setTimeout(() => toast.classList.remove('show'), 4000);
    }

    // Отправка формы
    const guestForm = document.getElementById('guestForm');
    guestForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const guestName = document.getElementById('guestName').value.trim();
        if (!guestName) return showToast('Пожалуйста, укажите ваше имя и фамилию.', true);
        const attendance = document.querySelector('input[name="attendance"]:checked');
        if (!attendance) return showToast('Пожалуйста, выберите, будете ли вы присутствовать.', true);
        const willAttend = attendance.value === 'yes';
        let companion = '', overnight = '', secondDay = '', overnightCount = '', secondDayOvernight = '';
        let drinks = [], transfer = [], companionDrinks = [];

        if (willAttend) {
            companion = document.getElementById('companionName').value.trim();
            document.querySelectorAll('#guestDrinksGroup input[type="checkbox"]:checked').forEach(cb => {
                drinks.push(cb.value);
            });
            document.querySelectorAll('input[name="companionDrinks"]:checked').forEach(cb => {
                companionDrinks.push(cb.value);
            });
            document.querySelectorAll('input[name="transfer"]:checked').forEach(cb => {
                transfer.push(cb.value);
            });
            const overnightYes = document.querySelector('input[name="overnightYes"]:checked');
            if (overnightYes && overnightYes.value === 'Да') {
                overnight = overnightYes.value;
                overnightCount = document.getElementById('overnightCount').value.trim();
            } else if (overnightYes && overnightYes.value === 'Нет') {
                overnight = 'Нет';
            }
            const sd = document.querySelector('input[name="secondDay"]:checked');
            if (sd) {
                secondDay = sd.value;
                if (secondDay === 'Да') {
                    const sdo = document.querySelector('input[name="secondDayOvernight"]:checked');
                    if (sdo) secondDayOvernight = sdo.value;
                }
            }
        }
        if (transfer.includes('Нет')) transfer = ['Нет'];

        fetch('/submit-guest', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                name: guestName,
                attendance: attendance.value,
                companion: companion,
                drinks: drinks,
                companionDrinks: companionDrinks,
                transfer: transfer,
                overnight: overnight,
                overnightCount: overnightCount,
                secondDay: secondDay,
                secondDayOvernight: secondDayOvernight
            })
        })
        .then(res => res.json())
        .then(data => {
            if (data.status === 'ok') {
                showToast(`Спасибо, ${guestName}! Ваш ответ отправлен организаторам. Ждём вас!`, false);
                document.getElementById('guestName').value = '';
                document.querySelectorAll('input[name="attendance"]').forEach(r => r.checked = false);
                document.getElementById('companionName').value = '';
                document.querySelectorAll('#guestDrinksGroup input[type="checkbox"]:checked').forEach(cb => cb.checked = false);
                document.querySelectorAll('input[name="companionDrinks"]:checked').forEach(cb => cb.checked = false);
                document.querySelectorAll('input[name="transfer"]:checked').forEach(cb => cb.checked = false);
                document.querySelectorAll('input[name="overnightYes"]').forEach(r => r.checked = false);
                document.getElementById('overnightCount').value = '';
                document.querySelectorAll('input[name="secondDay"]').forEach(r => r.checked = false);
                document.querySelectorAll('input[name="secondDayOvernight"]').forEach(r => r.checked = false);
                toggleExtraFields();
                toggleOvernightCount();
                toggleSecondDayOvernight();
                toggleCompanionAlcohol();
            } else {
                showToast('Ошибка отправки. Попробуйте позже.', true);
            }
        })
        .catch(error => {
            console.error(error);
            showToast('Ошибка отправки. Попробуйте позже.', true);
        });
    });
</script>
</body>
</html>
'''


@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)


@app.route('/submit-guest', methods=['POST'])
def submit_guest():
    data = request.json
    guest_name = data.get('name')
    attendance = data.get('attendance')
    companion = data.get('companion', '')
    drinks = data.get('drinks', [])
    companionDrinks = data.get('companionDrinks', [])
    transfer = data.get('transfer', [])
    overnight = data.get('overnight', '')
    overnightCount = data.get('overnightCount', '')
    secondDay = data.get('secondDay', '')
    secondDayOvernight = data.get('secondDayOvernight', '')

    text = f"📋 Новая анкета гостя:\n\n"
    text += f"👤 Имя: {guest_name}\n"
    text += f"✅ Присутствие: {'Да (приду)' if attendance == 'yes' else 'Нет (не смогу)'}\n"
    if companion: text += f"👥 Спутник(ца): {companion}\n"
    if drinks:
        text += f"🍷 Напитки гостя: {', '.join(drinks)}\n"
    else:
        text += f"🍷 Напитки гостя: не выбрано\n"
    if companionDrinks:
        text += f"🍷 Напитки спутника: {', '.join(companionDrinks)}\n"
    if transfer: text += f"🚗 Трансфер: {', '.join(transfer)}\n"
    if overnight:
        text += f"🏨 Ночёвка: {overnight}"
        if overnight == 'Да' and overnightCount:
            text += f" ({overnightCount} чел.)\n"
        else:
            text += "\n"
    if secondDay: text += f"🎉 Второй день: {secondDay}\n"
    if secondDayOvernight: text += f"🌙 Ночёвка на второй день: {secondDayOvernight}\n"

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    try:
        resp = requests.post(url, json={'chat_id': TELEGRAM_CHAT_ID, 'text': text, 'parse_mode': 'HTML'})
        resp.raise_for_status()
        return jsonify({'status': 'ok'}), 200
    except Exception as e:
        print(f"Ошибка отправки в Telegram: {e}")
        return jsonify({'status': 'error'}), 500


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)