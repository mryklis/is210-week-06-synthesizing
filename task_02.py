#!/usr/bin/env python
# -*- coding: utf-8 -*-


def prepare_email(appointments):
    format_string = 'Dear {},\nI look forward to meeting with you on {}.\nBest,\nMe'
    for obj in appointments:
        email = format_string.format(*appointments)
    return email
