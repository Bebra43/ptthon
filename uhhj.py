import webbrowser 

def obshenie():
    print('прив,я бот Disko')
    nach_razg = input('если хочешь узнать что происходит в стране пиши (новости),хочешь начать общение? Если это так то пиши (общение)')
    if nach_razg == 'новости':
        webbrowser.open('https://ria.ru/organization_YouTube_LLC/')
    if nach_razg == 'общение':
        temi = input('Мой ленивый но крутой разраб дабавил много тем если хочешь их увидеть пиши (темы)')
        if temi == 'нет':
            print('ок goodbye')
        if temi == 'темы':
            print('ок, вижу ты очень клевый ведь дошел аж до этого момента')
            temi_obshenie1 = input('выбирай тему смельчак):Аниме, Рисование, Музыка, игры, напитки, фразы.')
            if temi_obshenie1 == 'Аниме':
                print('Классный сайт для просмотра Аниме -> JUTSU.RU')
                print('Но ты ведь не за этим сюда пришел ты хочешь что то запрещенное ведь так?')
                print('Ахтунг 18+')
                webbrowser.open('https://www.youtube.com/watch?v=0AgTX1EAKAg')
            if temi_obshenie1 == 'Рисование':
                webbrowser.open('https://4brain.ru/draw/')
            if temi_obshenie1 == 'игры':
                print('Интересненько, есть несколько крутых и популярных игр сейчас или которые скоро выйдут')
                print('🧟Dying Light 2 Stay Human🧟 - Игра про мир в котором эпидемия, похожая на вирус зомби')
                print('Ну и другие игры, по типу: Horizon Forbidden West, Bendy and the Dark Revival, Hello Neighbor 2')
                print('А также: Atomic Heart, God of War Ragnarok и S.T.A.L.K.E.R. 2: Heart of Chernobyl')
                games_details = input('Выбери что ты хочешь увидеть(Описание игр или выйти(просто напиши что нибудь не по теме))').lower()
                if games_details == 'описание игр' or games_details == 'описание':
                        game_descriptioon == input('Введи название игры из вышеперечисленных(напиши главное правильно)').lower()
                if game_descriptioon == 'dying light 2 stay human':
                    print('Описание:')
                    webbrowser.open('https://ru.wikipedia.org/wiki/Dying_Light_2:_Stay_Human')
                elif game_descriptioon == 'horizon forbidden west':
                    print('Описание:')
                    webbrowser.open('https://ru.wikipedia.org/wiki/Horizon_Forbidden_West')
                elif game_descriptioon == 'bendy and the dark revival':
                    print('Описание:')
                    webbrowser.open('https://bendy-and-the-ink-machine.fandom.com/ru/wiki/Bendy_and_the_Dark_Revival')
                elif game_descriptioon == 'hello neighbor 2':
                    print('Описание:')
                    webbrowser.open('https://hello-neighbor-game.fandom.com/ru/wiki/Hello_Neighbor_2')
                elif game_descriptioon == 'atomic heart':
                    print('Описание:')
                    webbrowser.open('https://ru.wikipedia.org/wiki/Atomic_Heart')
                elif game_descriptioon == 'god of war ragnarok':
                    print('Описание:')
                    webbrowser.open('https://ru.wikipedia.org/wiki/God_of_War:_Ragnar%C3%B6k')
                elif game_descriptioon == 'stalker 2' or game_descriptioon == 's.t.a.l.k.e.r. 2: heart of chernobyl' or game_descriptioon == 'stalker 2: heart of chernobyl':
                    print('Описание:')
                    webbrowser.open('https://ru.wikipedia.org/wiki/S.T.A.L.K.E.R._2:_Heart_of_Chernobyl')
            else:
                print('Ты решил(а) пойти из темы игр, удачи')
                
obshenie()
