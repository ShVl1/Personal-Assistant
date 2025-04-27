from Bot import Bot


if __name__ == "__main__":
    bot = Bot()
    bot.book.load("auto_save")
    commands = ['Add', 'Search', 'Edit', 'Load', 'Remove', 'Save', 'Congratulate', 'View', 'Exit']
    
    bot.view.display_message('Hello. I am your contact-assistant. What should I do with your contacts?')
    
    try:
        bot.book.load("auto_save")
    except Exception as e:
        print(f"Note: Could not load saved data - {e}. Starting with empty address book.")
    
    commands = ['Add', 'Search', 'Edit', 'Load', 'Remove', 'Save', 'Congratulate', 'View', 'Exit']
    while True:
        action = input('Type help for list of commands or enter your command\n').strip().lower()
        if action == 'help':
            format_str = str('{:%s%d}' % ('^',20))
            for command in commands:
                print(format_str.format(command))
            action = input().strip().lower()
            bot.handle(action)
            if action in ['add', 'remove', 'edit']:
                bot.book.save("auto_save")
        else:
            bot.handle(action)
            if action in ['add', 'remove', 'edit']:
                bot.book.save("auto_save")
        if action == 'exit':
            break
