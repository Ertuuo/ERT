<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta
      name="viewport"
      content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0"
    />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <link rel="stylesheet" href="../static/css/style.css" />
    <title>Portföy</title>
  </head>
  <body>
    <header class="header">
      <nav class="header__nav main-nav">
        <ul class="main-nav__list main-list">
          <li class="main-list__item list-item">
            <a class="list-item__link" href="#home">HOME</a>
          </li>
          <li class="main-list__item list-item">
            <a class="list-item__link" href="#about">ABOUT</a>
          </li>
          <li class="main-list__item list-item">
            <a class="list-item__link" href="#skills">MY SKILLS</a>
          </li>
        </ul>
      </nav>
    </header>
    <main class="main">
      <!-- Önizleme bölümü -->
      <section class="main__home home" id="home">
        <h1 class="home__title">ERTUĞRUL DEMİRCİ</h1>
        <p class="home__subtitle">WEB-DEVELOPER, PYTHON PROGRAMMER, GAME-MAKER</p>
      </section>
      <!-- Hakkımda bölümü -->
      <section class="main__about about" id="about">
        <h2 class="about__title">ABOUT ME</h2>
        <div class="about__info info-block">
          <p class="info-block__text">
           Ben Ertuğrul. 12 yaşındyım. İstanbul'da yaşıyorum. Oyun, web siteleri ve benzeri
           pek çok şeyi yapabiliyorum. ŞU anda KODLAND üzerinden Python Basic kursunu bitirmiş bulunuyorum.
           Python Pro'yu ise bitirme yolundayım.
          </p>
          <img
            class="info-block__img"
            src="../static/img/profile.png"
            alt="me"
            width="250"
            height="250"
          />
        </div>
      </section>
      <!-- Beceriler bölümü -->
      <section class="main__skills skills" id="skills">
        <h2 class="skills__title">MY SKILLS</h2>
        <form action="/" method="POST">
          <ul class="skills__list skills-list">
            <li class="skills-list__skill skill">
              <img
                class="skill__img"
                src="../static/img/python.png"
                alt="python"
                width="150"
                height="150"
              />
              <span class="skill__info">Çevre Dostu Proje</span>
              <input class="skill__button" type="submit" name="button_python" value="SHOW PROJECT">
            </li>
            <li class="skills-list__skill skill">
              <img
                class="skill__img"
                src="../static/img/discord.png"
                alt="discord"
                width="150"
                height="150"
              />
              <span class="skill__info">Discord Botum</span>
              <input class="skill__button" type="submit" name="button_discord" value="SHOW PROJECT">
            </li>
            <li class="skills-list__skill skill">
              <img
                class="skill__img"
                src="../static/img/html.png"
                alt="html"
                width="150"
                height="150"
              />
              <span class="skill__info">Mem Oluşturucu</span>
              <input class="skill__button" type="submit" name="button_html" value="SHOW PROJECT">
            </li>
            <li class="skills-list__skill skill">
              <img
                class="skill__img"
                src="../static/img/db.webp"
                alt="SQL"
                width="150"
                height="150"
              />
              <span class="skill__info">Günlük</span>
              <input class="skill__button" type="submit" name="button_db" value="SHOW PROJECT">
            </li>
          </ul>
        </form>
        {% if button_python%}
          <div class="skills__project project" id="project">
              <img class="project__img" src="../static/img/python-project.png" alt="project" width="500">
              <a class="project__link" href="https://github.com/Ertuuo/Ertuuo/blob/main/ert.py">GitHub'da aç</a>
          </div>
  
        {% elif button_discord%} 
          <div class="skills__project project" id="project">
            <img class="project.png" src="../static/img/discord.png" alt="project" width="500">
            <a class="project__link" href="https://github.com/Ertuuo/Ertuuo/blob/main/ert.py">Bu Maalesef Açılmıyor</a>
        </div>
        
        {% elif button_html%}
          <div class="skills__project project" id="project">
              <img class="project__img" src="../static/img/html.png" alt="project" width="500">
              <a class="project__link" href="https://github.com/Ertuuo/Ertuuo/blob/main/ert.py">GitHub'da aç</a>
          </div>

        {% elif button_db%}
        <div class="skills__project project" id="project">
            <img class="project__img" src="../static/img/db.webd" alt="project" width="500">
            <a class="project__link" href="https://github.com/Ertuuo/Ertuuo/blob/main/ert.py">GitHub'da aç</a>
        </div>
      {% endif %}


      </section>
      <!-- Geri bildirim formu -->
      <section class="main__feedback feedback" id="feedback">
        <h2 class="feedback__title">FEEDBACK</h2>
        <form action="" method="POST" class="feedback__form form">
          <label for="email">
            <input type="email" class="form__input" name="email" id="email" placeholder="Введите E-mail" required>
          </label>
          <label for="text">
            <textarea name="text" class="form__input" id="text" cols="70" rows="10" required placeholder="Comment"></textarea>
          </label>
          <button class="form__button" type="submit">SEND</button>
        </form>
      </section>
    </main>
    <!-- Sosyal medya bağlantıları için bir alt bilgi -->
    <footer>

    </footer>
  </body>
</html>
