#!/usr/bin/env python
# encoding: utf-8

import os
import telegram
import unittest

from token import TOKEN


@unittest.skipIf(not TOKEN, "No tokens provided")
class BotTest(unittest.TestCase):
    def setUp(self):
        bot = telegram.Bot(token=os.environ.get('TOKEN'))
        self._bot = bot
        print 'Testing the Bot API class'

    def testGetMe(self):
        '''Test the telegram.Bot getMe method'''
        print 'Testing getMe'
        user = self._bot.getMe()
        self.assertEqual(120405045, user.id)
        self.assertEqual('Toledo\'s Palace Bot', user.first_name)
        self.assertEqual(None, user.last_name)
        self.assertEqual('ToledosPalaceBot', user.username)

    def testSendMessage(self):
        '''Test the telegram.Bot sendMessage method'''
        print 'Testing sendMessage'
        message = self._bot.sendMessage(chat_id=12173560,
                                        text=u'Моё судно на воздушной подушке полно угрей'.encode('utf8'))
        self.assertEqual(u'Моё судно на воздушной подушке полно угрей', message.text)

    def testGetUpdates(self):
        '''Test the telegram.Bot getUpdates method'''
        print 'Testing getUpdates'
        updates = self._bot.getUpdates()
        self.assertEqual(129566481, updates[0].update_id)

    def testForwardMessage(self):
        '''Test the telegram.Bot forwardMessage method'''
        print 'Testing forwardMessage'
        message = self._bot.forwardMessage(chat_id=12173560,
                                           from_chat_id=12173560,
                                           message_id=138)
        self.assertEqual(u'Oi', message.text)
        self.assertEqual(u'leandrotoledo', message.forward_from.username)

    # def testSendPhoto(self):
    #     '''Test the telegram.Bot sendPhoto method'''
    #     print 'Testing sendPhoto'
    #     message = self._bot.sendPhoto()
