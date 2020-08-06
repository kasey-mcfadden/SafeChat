VER = '0.2'
from sms import sendSMS, rentSMS
from dynamo import dynamo_put, dynamo_get
from demo import convo

# interpreter
def interpreter(text, msisdn, v_num):
    send_to = msisdn    # user number
    send_from = v_num   # virtual number provided by Nexmo

    # default reply assuming unknown phrase
    print('Message: "%s" from %s' % (text, msisdn))
    reply = 'I don\'t know how to interpret that. Try asking me to sign up or add a new context.'

    # intent = register
    regPhr = ['register', 'join', 'Register', 'Join', 'sign up', 'Sign up']
    for phrase in regPhr:
        if phrase in text:
            v_num = rentSMS()
            response = dynamo_put(msisdn, v_num)
            v_nums = dynamo_get(msisdn)
            reply = "Hello, %s. Your virtual number(s): %s" % (msisdn, v_nums)
            """
                Do something with new user registration
            """


    # intent = context2
    cxtPhr = ['Context', 'context', 'create context', 'Create context', 'add context', 'Add context', 'new context', 'New context']
    for phrase in cxtPhr:
        if phrase in text:
            v_nums = dynamo_get(msisdn)
            reply = "Hello, %s. Your virtual number(s): %s" % (msisdn, v_nums)
            """
                Do something with context
            """

    # format for outgoing bot texts
    outgoing = "---- Safe Chat ----\n~~ v%s ~~\n\n%s" % (VER, reply)

    sent = sendSMS(send_to, send_from, outgoing)
    return sent
