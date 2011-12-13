import web

render = web.template.render('templates/')

urls = ('/', 'index',
        '/(\d+)', 'index')
db = web.database(dbn='sqlite', db='/home/jrenaut/src/sqlite/bikes.db')

app = web.application(urls, globals())


class index:
    def GET(self, q_id=None):
        if q_id == None:
            q_id = 1
        limvar = dict(q_id=q_id)
        question = db.select('question', limvar, where="id=$q_id")[0]        
        answers = db.select('answer', limvar, where="p_question_id=$q_id")
        return render.index(question, answers)
        
if __name__ == "__main__": app.run()
        