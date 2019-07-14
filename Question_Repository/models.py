from django.db import models

# Create your models here.
class choice_question(models.Model):
    '''
    question: 题目文本内容，markdown格式
    options： json 格式为{'A':www, 'B':xxx, 'C':yyy, 'D':zzz}
    answer: char A B C D
    '''
    question_id = models.AutoField(primary_key=True)
    question = models.TextField()
    options = models.TextField()
    answer = models.CharField(max_length=1)
    def get_data_by_id(cls, question_id):
        question = cls.objects.get(question_id = question_id)
        data = {
                'question' : question.question,
                'options' : question.options,
                'answer' : question.answer
                }
        return {'data':data}


class fillblank_question(models.Model):
    '''
    question: 题目文本内容，markdown格式
    answer: markdown格式
    '''
    question_id = models.AutoField(primary_key=True)
    question = models.TextField()
    answer = models.CharField(max_length=100)
    def get_data_by_id(cls, question_id):
        question = cls.objects.get(question_id = question_id)
        data = {
                'question' : question.question,
                'answer' : question.answer
                }
        return {'data':data}

class comprehensive_question(models.Model):
    '''
    question: 题目文本内容，markdown格式
    answer: markdown格式
    '''
    question_id = models.AutoField(primary_key=True)
    question = models.TextField()
    answer = models.TextField()
    def get_data_by_id(cls, question_id):
        question = cls.objects.get(question_id = question_id)
        data = {
                'question' : question.question,
                'answer' : question.answer
                }
        return {'data':data}