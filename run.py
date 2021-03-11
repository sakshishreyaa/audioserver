from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy
# from flask_restful import Resource, Api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

@app.route('/<string:audioFileType>', defaults={'audioFileId': None},methods=['GET','POST','PUT','DELETE'])
@app.route('/<string:audioFileType>/<string:audioFileId>',methods=['GET','POST','PUT','DELETE'])
def audioserver(audioFileType,audioFileId):
    
    try:
        if audioFileType and audioFileType.lower() in ('song','podcast','audiobook'):
            if audioFileId and int(audioFileId):

                return jsonify({'audioFileType': audioFileType,'audioFileId':audioFileId}),200

                # return jsonify({'status':'error','message':'not a valid url specify file type'}),400
            if request.method=='GET':
                return jsonify({'audioFileType': audioFileType,'audioFileId':audioFileId}),200

                # return jsonify({'audioFileType': audioFileType}),200
            elif request.method=='POST':
                pass
            elif request.method=='PUT':
                pass
            else:
                pass
        if request.method=='GET':
            pass
        elif request.method=='POST':
            pass
        elif request.method=='PUT':
            pass
        else:
            pass
    except Exception as e:
        return jsonify({'status':'error','message':f'unexpected error occured {e}'}),500




class Audio:
    def __init__(self,_id,name,duration,upload_time,_type):
        self._id=_id
        self.name=name
        self.duration=duration
        self.upload_time=upload_time
        self._type=_type
    
    def create(self):
        audio = Audio(**kwargs)
        db.session.add(audio)
        db.session.commit()

    def update(self,**kwargs):
        audio=Audio()

    def output(self):
        
        return {
            'id':self._id,
            'name':self.name,
            'duration':self.duration,
            'type':self._type,
            'upload_time':self.upload_time,
        }

class Song(Audio):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.kwargs=kwargs
    def create(self):
        audio = Audio(**self.kwargs)
        db.session.add(audio)
        db.session.commit()
    def output(self):
        return self.kwargs

class PodCast(Audio):
    def __init__(self,**kwargs):
        ukwargs ={k : v for k ,v in ukwargs.items() if k in ('_id','name','duration','upload_time')}

        super().__init__(**ukwargs)
        self.host=kwargs['host']
        self.participants=kwargs.get('participants',None)
    def create(self):
        audio = Audio(**self.kwargs)
        db.session.add(audio)
        db.session.commit()
    def output(self):
        return self.kwargs

class AudioBook(Audio):
    def __init__(self,**kwargs):
        ukwargs ={k , v for k ,v in ukwargs.items() if k in ('_id','name','duration','upload_time')}

        super().__init__(**ukwargs)
        self.author=kwargs['author']
        self.narrator=kwargs['narrator']
    def create(self):
        audio = Audio(**self.kwargs)
        db.session.add(audio)
        db.session.commit()
    def output(self):
        return self.kwargs


if __name__ == '__main__':
    app.run(debug=True)