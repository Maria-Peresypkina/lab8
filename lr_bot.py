import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext, filters
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from telegram import ReplyKeyboardMarkup, KeyboardButton

# Логггги
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# БДшечка
engine = create_engine('sqlite:///user_responses.db')
Base = declarative_base()

class UserResponse(Base):
    __tablename__ = 'user_responses'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    question_number = Column(Integer)
    answer = Column(String)

Base.metadata.create_all(engine)

# Функция для сохранения ответов пользователя в базу данных
def save_user_response(user_id, question_number, answer):
    Session = sessionmaker(bind=engine)
    session = Session()
    user_response = UserResponse(user_id=user_id, question_number=question_number, answer=answer)
    session.add(user_response)
    session.commit()

async def handle_message(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    question_number = context.user_data.get('question_number', 1)
    answer = update.message.text
    res = context.user_data.get('res', 0)
    type = 'рыба фугу'
    save_user_response(user_id, question_number, answer)
    context.user_data['question_number'] = question_number + 1
    context.user_data['res'] = res
    if question_number == 20:
        if res < -15:
            type = 'рыба фугу'
        elif res < -5:
            type = 'треска'
        elif res < 5:
            type = 'рыбка Дори'
        elif res < 15:
            type = 'рыба молот'
        else:
            type = 'aкула'
        result = 'Спасибо за ответы! Твой тип личности - ' + type
        await context.bot.send_message(chat_id=update.effective_chat.id, text=result) 
        context.user_data.clear()
    else:
        if question_number == 1:
            keyboard = [
                [KeyboardButton('да'), KeyboardButton('нет'), KeyboardButton('Не знаю')]
            ]
            reply_markup = ReplyKeyboardMarkup(keyboard)
            next_question = 'Вопрос 1: Чувствуете ли вы тревогу?'
            await context.bot.send_message(chat_id=update.effective_chat.id, text=next_question, reply_markup=reply_markup)
        elif question_number == 2:
            if answer.lower() == 'да':
                res=res+1
                keyboard = [
                    [KeyboardButton('да'), KeyboardButton('нет'), KeyboardButton('Не знаю')]
                ]
                reply_markup = ReplyKeyboardMarkup(keyboard)
                next_question = 'Вопрос 2: Способны ли вы сами справиться с тревогой?'
                await context.bot.send_message(chat_id=update.effective_chat.id, text=next_question, reply_markup=reply_markup)
            elif answer.lower() == 'нет':
                res=res-1
                keyboard = [
                    [KeyboardButton('да'), KeyboardButton('нет'), KeyboardButton('Не знаю')]
                ]
                reply_markup = ReplyKeyboardMarkup(keyboard)
                next_question = 'Вопрос 2: Помогаете ли вы близким справиться с тревогой?'
                await context.bot.send_message(chat_id=update.effective_chat.id, text=next_question, reply_markup=reply_markup)
            else:
                keyboard = [
                    [KeyboardButton('да'), KeyboardButton('нет'), KeyboardButton('Не знаю')]
                ]
                reply_markup = ReplyKeyboardMarkup(keyboard)
                next_question = 'Вопрос 2: Находитесь ли вы в гармонии с собой?'
                await context.bot.send_message(chat_id=update.effective_chat.id, text=next_question, reply_markup=reply_markup)
        elif question_number == 3:
            if answer.lower() == 'да':
                res=res+1
                keyboard = [
                    [KeyboardButton('да'), KeyboardButton('нет'), KeyboardButton('Не знаю')]
                ]
                reply_markup = ReplyKeyboardMarkup(keyboard)
                next_question = 'Вопрос 3: Иногда вам хочется закрыться от всех?'
                await context.bot.send_message(chat_id=update.effective_chat.id, text=next_question, reply_markup=reply_markup)
            elif answer.lower() == 'нет':
                res=res-1
                keyboard = [
                    [KeyboardButton('да'), KeyboardButton('нет'), KeyboardButton('Не знаю')]
                ]
                reply_markup = ReplyKeyboardMarkup(keyboard)
                next_question = 'Вопрос 3: Вы открыты к окружающим?'
                await context.bot.send_message(chat_id=update.effective_chat.id, text=next_question, reply_markup=reply_markup)
            else:
                keyboard = [
                    [KeyboardButton('да'), KeyboardButton('нет'), KeyboardButton('Не знаю')]
                ]
                reply_markup = ReplyKeyboardMarkup(keyboard)
                next_question = 'Вопрос 3: Вы часто высказываете своё мнение?'
                await context.bot.send_message(chat_id=update.effective_chat.id, text=next_question, reply_markup=reply_markup)
        elif question_number == 4:
            if answer.lower() == 'да':
                res=res+1
                keyboard = [
                    [KeyboardButton('да'), KeyboardButton('нет'), KeyboardButton('Не знаю')]
                ]
                reply_markup = ReplyKeyboardMarkup(keyboard)
                next_question = 'Вопрос 4: Вам комфортно наедине с собой?'
                await context.bot.send_message(chat_id=update.effective_chat.id, text=next_question, reply_markup=reply_markup)
            elif answer.lower() == 'нет':
                res=res-1
                keyboard = [
                    [KeyboardButton('да'), KeyboardButton('нет'), KeyboardButton('Не знаю')]
                ]
                reply_markup = ReplyKeyboardMarkup(keyboard)
                next_question = 'Вопрос 4: Вам комфортно наедине с собой?'
                await context.bot.send_message(chat_id=update.effective_chat.id, text=next_question, reply_markup=reply_markup)
            else:
                keyboard = [
                    [KeyboardButton('да'), KeyboardButton('нет'), KeyboardButton('Не знаю')]
                ]
                reply_markup = ReplyKeyboardMarkup(keyboard)
                next_question = 'Вопрос 4: Вам комфортно наедине с собой?'
                await context.bot.send_message(chat_id=update.effective_chat.id, text=next_question, reply_markup=reply_markup)
        elif question_number == 5:
            if answer.lower() == 'да':
                res=res+1
            elif answer.lower() == 'нет':
                res=res-1
            keyboard = [
                [KeyboardButton('да'), KeyboardButton('нет'), KeyboardButton('Не знаю')]
            ]
            reply_markup = ReplyKeyboardMarkup(keyboard)
            next_question = 'Вопрос 5: Вы можете высказывать мнение против большинства?'
            await context.bot.send_message(chat_id=update.effective_chat.id, text=next_question, reply_markup=reply_markup)
        elif question_number == 6:
            if answer.lower() == 'да':
                res=res+1
            elif answer.lower() == 'нет':
                res=res-1
            keyboard = [
                [KeyboardButton('да'), KeyboardButton('нет'), KeyboardButton('Не знаю')]
            ]
            reply_markup = ReplyKeyboardMarkup(keyboard)
            next_question = 'Вопрос 6: Если кто-то будет некорректно себя вести, вы ему об этом скажете?'
            await context.bot.send_message(chat_id=update.effective_chat.id, text=next_question, reply_markup=reply_markup)
        elif question_number == 7:
            if answer.lower() == 'да':
                res=res+1
            elif answer.lower() == 'нет':
                res=res-1
            keyboard = [
                [KeyboardButton('да'), KeyboardButton('нет'), KeyboardButton('Не знаю')]
            ]
            reply_markup = ReplyKeyboardMarkup(keyboard)
            next_question = 'Вопрос 7: Вы часто можете отвлечься на что-то и забыть про все дела?'
            await context.bot.send_message(chat_id=update.effective_chat.id, text=next_question, reply_markup=reply_markup)
        elif question_number == 8:
            if answer.lower() == 'да':
                res=res+1
            elif answer.lower() == 'нет':
                res=res-1
            keyboard = [
                [KeyboardButton('да'), KeyboardButton('нет'), KeyboardButton('Не знаю')]
            ]
            reply_markup = ReplyKeyboardMarkup(keyboard)
            next_question = 'Вопрос 8: В спорах вы будете стоять до конца, даже если не правы?'
            await context.bot.send_message(chat_id=update.effective_chat.id, text=next_question, reply_markup=reply_markup)
        elif question_number == 9:
            if answer.lower() == 'да':
                res=res+1
            elif answer.lower() == 'нет':
                res=res-1
            keyboard = [
                [KeyboardButton('да'), KeyboardButton('нет'), KeyboardButton('Не знаю')]
            ]
            reply_markup = ReplyKeyboardMarkup(keyboard)
            next_question = 'Вопрос 9: У вас есть много достижений, которыми вы гордитесь?'
            await context.bot.send_message(chat_id=update.effective_chat.id, text=next_question, reply_markup=reply_markup)
        elif question_number == 10:
            if answer.lower() == 'да':
                res=res+1
            elif answer.lower() == 'нет':
                res=res-1
            keyboard = [
                [KeyboardButton('да'), KeyboardButton('нет'), KeyboardButton('Не знаю')]
            ]
            reply_markup = ReplyKeyboardMarkup(keyboard)
            next_question = 'Вопрос 10: Вам сложно представить себя другим людям?'
            await context.bot.send_message(chat_id=update.effective_chat.id, text=next_question, reply_markup=reply_markup)
        elif question_number == 11:
            if answer.lower() == 'да':
                res=res+1
            elif answer.lower() == 'нет':
                res=res-1
            keyboard = [
                [KeyboardButton('да'), KeyboardButton('нет'), KeyboardButton('Не знаю')]
            ]
            reply_markup = ReplyKeyboardMarkup(keyboard)
            next_question = 'Вопрос 11: Вы очень часто так погружаетесь в свои мысли, что не замечаете или забываете об окружающих вас людях?'
            await context.bot.send_message(chat_id=update.effective_chat.id, text=next_question, reply_markup=reply_markup)
        elif question_number == 12:
            if answer.lower() == 'да':
                res=res+1
            elif answer.lower() == 'нет':
                res=res-1
            keyboard = [
                [KeyboardButton('да'), KeyboardButton('нет'), KeyboardButton('Не знаю')]
            ]
            reply_markup = ReplyKeyboardMarkup(keyboard)
            next_question = 'Вопрос 12: Вы стараетесь, по возможности, сразу же ответить на все электронные письма и не можете выдержать беспорядок в папке “Входящие”'
            await context.bot.send_message(chat_id=update.effective_chat.id, text=next_question, reply_markup=reply_markup)
        elif question_number == 13:
            if answer.lower() == 'да':
                res=res+1
            elif answer.lower() == 'нет':
                res=res-1
            keyboard = [
                [KeyboardButton('да'), KeyboardButton('нет'), KeyboardButton('Не знаю')]
            ]
            reply_markup = ReplyKeyboardMarkup(keyboard)
            next_question = 'Вопрос 13: Вы, как правило, не начинаете разговор'
            await context.bot.send_message(chat_id=update.effective_chat.id, text=next_question, reply_markup=reply_markup)
        elif question_number == 14:
            if answer.lower() == 'да':
                res=res+1
            elif answer.lower() == 'нет':
                res=res-1
            keyboard = [
                [KeyboardButton('да'), KeyboardButton('нет'), KeyboardButton('Не знаю')]
            ]
            reply_markup = ReplyKeyboardMarkup(keyboard)
            next_question = 'Вопрос 14: Вы редко делаете что-то из чистого любопытства'
            await context.bot.send_message(chat_id=update.effective_chat.id, text=next_question, reply_markup=reply_markup)
        elif question_number == 15:
            if answer.lower() == 'да':
                res=res+1
            elif answer.lower() == 'нет':
                res=res-1
            keyboard = [
                [KeyboardButton('да'), KeyboardButton('нет'), KeyboardButton('Не знаю')]
            ]
            reply_markup = ReplyKeyboardMarkup(keyboard)
            next_question = 'Вопрос 15: Я считаю, что правила существуют для того, чтобы их нарушать, и у меня были проблемы с законом'
            await context.bot.send_message(chat_id=update.effective_chat.id, text=next_question, reply_markup=reply_markup)
        elif question_number == 16:
            if answer.lower() == 'да':
                res=res+1
            elif answer.lower() == 'нет':
                res=res-1
            keyboard = [
                [KeyboardButton('да'), KeyboardButton('нет'), KeyboardButton('Не знаю')]
            ]
            reply_markup = ReplyKeyboardMarkup(keyboard)
            next_question = 'Вопрос 16: Я постоянно нахожусь в приподнятом настроении, отрицаю печаль и грусть'
            await context.bot.send_message(chat_id=update.effective_chat.id, text=next_question, reply_markup=reply_markup)
        elif question_number == 17:
            if answer.lower() == 'да':
                res=res+1
            elif answer.lower() == 'нет':
                res=res-1
            keyboard = [
                [KeyboardButton('да'), KeyboardButton('нет'), KeyboardButton('Не знаю')]
            ]
            reply_markup = ReplyKeyboardMarkup(keyboard)
            next_question = 'Вопрос 17: Я женственная, миловидная (для женщин) ИЛИ Я выгляжу гораздо моложе своего возраста, можно сказать, по-юношески (для мужчин)'
            await context.bot.send_message(chat_id=update.effective_chat.id, text=next_question, reply_markup=reply_markup)
        elif question_number == 18:
            if answer.lower() == 'да':
                res=res+1
            elif answer.lower() == 'нет':
                res=res-1
            keyboard = [
                [KeyboardButton('да'), KeyboardButton('нет'), KeyboardButton('Не знаю')]
            ]
            reply_markup = ReplyKeyboardMarkup(keyboard)
            next_question = 'Вопрос 18: Я принципиален, могу отстаивать свои права, даже судиться, особенно, если вижу, что меня игнорируют или не уважают или ведут себя несправедливо'
            await context.bot.send_message(chat_id=update.effective_chat.id, text=next_question, reply_markup=reply_markup)
        elif question_number == 19:
            if answer.lower() == 'да':
                res=res+1
            elif answer.lower() == 'нет':
                res=res-1
            keyboard = [
                [KeyboardButton('да'), KeyboardButton('нет'), KeyboardButton('Не знаю')]
            ]
            reply_markup = ReplyKeyboardMarkup(keyboard)
            next_question = 'Вопрос 19: У меня богатый внутренний мир, я умею уходить в мир фантазий и мне там спокойно'
            await context.bot.send_message(chat_id=update.effective_chat.id, text=next_question, reply_markup=reply_markup)
        else:
            next_question = f'Вопрос {question_number + 1}: ...'
        update.message.reply_text(next_question)
        context.user_data['res'] = res

async def stop(update, context):
    """Остановить бота"""
    await context.bot.send_message(chat_id=update.effective_chat.id, 
                                   text='Бот остановлен.')
    context.bot.stop()

async def start(update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, 
                                   text="Добрый день, я могу определить ваш тип личности! Напишите что-то, если хотите начать=)")

if __name__ == '__main__':
    TOKEN = '6642972125:AAFH5t3_iJ5QPb_OInGs9k6qK4qKSrd4ZJg'
    # создание экземпляра бота через `ApplicationBuilder`
    application = ApplicationBuilder().token(TOKEN).build()
    stop_handler = CommandHandler('stop', stop)
    application.add_handler(stop_handler)
    # создаем обработчик для команды '/start'
    start_handler = CommandHandler('start', start)
    # регистрируем обработчик в приложение
    application.add_handler(start_handler)
    # создаем обработчик для сообщений от пользователя
    message_handler = MessageHandler(filters.TEXT & ~ filters.COMMAND, handle_message)
    # регистрируем обработчик в приложение
    application.add_handler(message_handler)
    # запускаем приложение    
    application.run_polling()