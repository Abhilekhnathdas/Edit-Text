from flask import Flask, render_template, request,redirect,url_for

app = Flask(__name__)


@app.route('/home')
def home():
    sentences=getsentences()
    newsntnces = ''

    #convert each sentence into button so that it becomes clickable.

    for i in range(len(sentences)):
        newsntnces = newsntnces + '<button class="edit" name='+str(i)+'>' + sentences[i] + '</button>'
    return render_template('edit_text.html', newsentences=newsntnces)

@app.route('/edit',methods=['GET', 'POST'])
def edit():
    try:
       if request.method == 'POST':
          edited_text= request.form.get("sel_text")
          ind=int(request.form.get("index"))
          sentences=getsentences()
          sentences[ind]=edited_text
          s=' '.join(sentences)
          fc = open("statements","w")
          fc.writelines(s)
          return redirect(url_for('home'))
    except:
        return 'gvccv'


# It will break the whole text into paragraphs of 20 words each.

def getsentences():
    fc = open("statements")
    sentences = fc.readlines()
    complete = ''.join(sentences).split(' ')
    eq_len_sen = []
    for i in range(0, len(complete), 20):
        k = complete[i:i + 20]
        eq_len_sen.append(' '.join(k))
    return eq_len_sen

if __name__ == '__main__':
    app.run()
