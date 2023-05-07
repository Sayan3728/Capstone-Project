from flask import Flask,request,jsonify
from flask_restful import Api,Resource
from flask_sqlalchemy import SQLAlchemy
import json
import mysql.connector


app = Flask(__name__)

cnx = mysql.connector.connect(user="root", password="*Green123#", host="127.0.0.1")
cur = cnx.cursor(buffered=True)
cur.execute("CREATE DATABASE IF NOT EXISTS aapDB")
cur.close()
cnx.close()


canditure=[{
        "candidateid":1,
        "fullname": "Joel Oram",
        "skillset":["java","spring-boot","docker","kubernetes"]
    }
]


db_uri="mysql://root:*Green123#@Localhost/aapDB"
#I am going to use ORM to interact with the databases, so it needs to be setup.
app.config["SQLALCHEMY_DATABASE_URI"]=db_uri
app.config["SQLALCHEMY_TRACK_MODIFICATION"]=False
db=SQLAlchemy(app)#rap app class with SQLALchemy
api=Api(app)

class ReqTB(db.Model):
  CandId=db.Column(db.String(100),primary_key=True,nullable=False)
  FullName = db.Column(db.String(100), default="NA")
  skillset= db.Column(db.String(300),default="NA")
#instruct SQlAchemy to create the table
db.create_all()

for candi in canditure:
    candid= candi.get("candidateid") if candi.get("candidateid") else "NA"
    fullname= candi.get("fullname") if candi.get("fullname") else "NA"
    (candi["skillset"]).sort()
    ski2=str((candi["skillset"]))

    req = ReqTB(CandId=candid,FullName=fullname,skillset=ski2)
    if not ReqTB.query.filter_by(CandId=candid).all():
        db.session.add(req)  # adding the oject or instance in the table means adding a row in table
        db.session.commit()
    print(candid,fullname,ski2,type(req))

class canditure(Resource):
    def get(self):
        args = request.args
        skill_required = args.get("skillset")
        # country_required=country
        print(skill_required)
        detail = ReqTB.query.filter_by(skillset=skill_required).all()
        print("detail type",type(detail))
        if detail:

            return {"CandId": detail[0].CandId, "FullName": detail[0].FullName, "skillset":detail[0].skillset}
        else:
            return {"message": "the specified Candidate is  not in the list"}
    def post(self):
        data = request.get_json()
        CandId = data['CandId']
        # print("CandId type",type(CandId))
        # print("data type", type(data))
        detail = ReqTB.query.filter_by(CandId=CandId).all()
        if detail:
            return {"message": "The specified country is already in the list"},404
        else:
             (data["skillset"]).sort()
             curr = ReqTB(CandId=data['CandId'],FullName=data['FullName'],skillset=str(data["skillset"]))
             db.session.add(curr)
             db.session.commit()
             return {"message": "Details addedd to the data base"}

    def put(self):
        data = request.get_json()
        CandId= data['CandId']
        detail = ReqTB.query.filter_by(CandId=CandId).all()
        if detail:
            x = ReqTB.query.filter_by(CandId=CandId).first()
            x.FullName= data['FullName']
            (data['skillset']).sort()
            x.skillset= str(data['skillset'])
            db.session.commit()
            return {"message": "Details updated to the data base"}
        else:
            return {"message": "The specified coandidate is already in the list"}
    def delete(self):
        args = request.args
        CandId = args.get("CandId")
        detail = ReqTB.query.filter_by(CandId=CandId).all()
        if detail:
            detail[0].skillset="MARKED"
            db.session.commit()
            return{'message': "Marked"}
        else:
            {"message": "The specified coandidate is already in the list"}
class Match(Resource):
    def post(self,a=None):
        if a:
            print("Called yaar")
            data=a
        else:

            data = request.get_json()
        requiredSkillset = data['requiredSkillsets']
        # print(requiredSkillset)
        # print(type(requiredSkillset))
        requiredSkillset.sort()
        s2=str(requiredSkillset)
        ss=s2[1:len(s2) - 1]
        # print(ss)
        s1 = ss.replace("'", "")
        s11 = s1.replace(" ", "")
        l = s11.split(",")
        detaild=[]
        for r in l:
            rocky = ReqTB.query.filter(ReqTB.skillset.contains(r)).all()
            print(r)
            detaild.extend(rocky)
        se2=set(detaild)
        detail=list(se2)
        for r in detail:
            print(r.FullName)

        if detail:
            #print(len(detail))
            d1={"total candidate found":len(detail)}
            l1=[d1]
            for d in detail:
                 S1=d.skillset
                 s = S1[1:len(S1) - 1]
                 s1 = s.replace("'","")
                 s11=s1.replace(" ","")

                 l=s11.split(",")#skillset list
                 s2 = str(requiredSkillset)
                 ss = s2[1:len(s2) - 1]
                 s3=ss.replace("'","")
                 s33=s3.replace(" ","")
                 # print("s3",s3)
                 l2=s33.split(",")#requiredskill list
                 l3=[]
                 for i in l:
                     for j in l2:
                         if(i==j):
                             l3.append(i)
                 percentage = (len(l3) / len(l2)) * 100
                 c={"CandId": d.CandId, "FullName": d.FullName, "skillset":l,"Profile-match":percentage}
                 l1.append(c)

            return l1
        else:
             return {"message": "the specified Candidate is  not in the list"}

class internal(Resource):
    def post(self):
        data = request.get_json()
        CandId = data['CandId']
        # print("CandId type",type(CandId))
        # print("data type", type(data))
        detail = ReqTB.query.filter_by(CandId=CandId).all()
        if detail:
            return {"message": "The specified country is already in the list"}, 404
        else:
            (data["skillset"]).sort()
            curr = ReqTB(CandId=data['CandId'], FullName=data['FullName'], skillset=str(data["skillset"]))
            db.session.add(curr)
            db.session.commit()
            return {"message": "Details addedd to the data base"}

class inter(Resource):

    def post(self):
        l1 = []
        w=0
        data = request.get_json()
        data1=data
        requiredSkillset = data['requiredSkillsets']
        optionalSkillset = data['optionalSkillsets']
        l11=optionalSkillset+requiredSkillset
        l11.sort()
        s2 = str(l11)
        ss = s2[1:len(s2) - 1]
        # print(ss)
        s1 = ss.replace("'", "")
        s11 = s1.replace(" ", "")
        l = s11.split(",")
        detaild = []
        for r in l:
            rocky = ReqTB.query.filter(ReqTB.skillset.contains(r)).all()
            print(r)
            detaild.extend(rocky)
            w=+1
        se2 = set(detaild)
        detail = list(se2)
        for r in detail:
            print(r.FullName)
        if detail:
            print(len(detail))
            d1={"total candidate found":len(detail)}
            l1=[d1]
            for d in detail:
                 S1=d.skillset
                 s = S1[1:len(S1) - 1]
                 s1 = s.replace("'","")
                 s11=s1.replace(" ","")

                 l=s11.split(",")#skillset list
                 s2 = str(l11)
                 ss = s2[1:len(s2) - 1]
                 s3=ss.replace("'","")
                 s33=s3.replace(" ","")
                 # print("s3",s3)
                 l2=s33.split(",")#requiredskill list
                 print(l2)
                 l3 = []
                 for i in l:
                     for j in l2:
                         if (i == j):
                             l3.append(i)
                 percentage = (len(l3) / len(l2)) * 100

                 c={"CandId": d.CandId, "FullName": d.FullName, "skillset":l,"percentage":percentage}
                 if(c["percentage"]==100):


                    l1.append(c)






                 elif(c["percentage"]<=100):
                    print("second")
                    requiredSkillset = data['requiredSkillsets']
                    requiredSkillset.sort()
                    s2 = str(requiredSkillset)
                    ss = s2[1:len(s2) - 1]
                    ss1=ss.replace("'","")
                    ss2=ss1.replace(" ","")
                    l=ss2.split(",")
                    detaild = []
                    for r in l:
                        rocky = ReqTB.query.filter(ReqTB.skillset.contains(r)).all()
                        print(r)
                    detaild.extend(rocky)
                    se2 = set(detaild)
                    detail = list(se2)
                    if detail:
                        d1 = {"total candidate found": len(detail)}
                        l1 = [d1]
                        for d in detail:
                            S1 = d.skillset
                            s = S1[1:len(S1) - 1]
                            s1 = s.replace("'", "")
                            s11 = s1.replace(" ", "")

                            l = s11.split(",")  # skillset list
                            s2 = str(requiredSkillset)
                            ss = s2[1:len(s2) - 1]
                            s3 = ss.replace("'", "")
                            s33 = s3.replace(" ", "")
                    # print("s3",s3)
                            l2 = s33.split(",")  # requiredskill list
                            l3 = []
                            for i in l:
                                for j in l2:
                                    if (i == j):
                                        l3.append(i)
                            percentage = (len(l3) / len(l2)) * 100

                            c = {"CandId": d.CandId, "FullName": d.FullName, "skillset": l, "percentage": percentage}
                            l1.append(c)
                    return l1
        # # elif(len(detail)==0):
        #     print("third")
        #
        #     obj1=Match()
        #     obj1.post(data1)


api.add_resource(canditure,'/app')
api.add_resource(Match,'/req')
api.add_resource(internal,'/int')
api.add_resource(inter,'/internal')
if __name__=="__main__":
    app.run(host="127.0.0.1",port=9000,debug=True)