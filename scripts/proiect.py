import json
inputfile="misiune.e"
outputfile="orbitaa.czml"

def convert_czml():
    datapoints=[]
    start=False

    try:
        with open(inputfile, "r") as f:
            for line in f:
                line=line.strip()

                if line == "EphemerisTimePosVel":
                    start=True
                    continue
                if start and line:
                    parts=line.split()
                    if len(parts) >=4:
                        t=float(parts[0])
                        x=float(parts[1])
                        y=float(parts[2])
                        z=float(parts[3])
                        datapoints.append([t,x,y,z])
        
        start_time="2026-02-19T21:00:00Z"
        czml=[
            {"id": "document", "version": "1.0"},
            {
                "id":"Satelit_Gmat",
                "availability":f"{start_time}/2026-02-19T23:00:00Z",
                "position": {
    "interpolationAlgorithm": "HERMITE", 
    "interpolationDegree": 2,
    "epoch": start_time,
    "cartesian": []
},
"point": {
    "color": {"rgba": [255, 255, 255, 255]},
    "pixelSize": 10,
    "outlineColor": {"rgba": [0, 0, 0, 255]},
    "outlineWidth": 2
},
                "path":{
                    "show":True,
                    "width":2,
                    "material":{"solidColor":{"color":{"rgba":[0,255,255,255]}}}
                }
            }
        ]
        
        for p in datapoints:
            czml[1]["position"]["cartesian"].extend([p[0],p[1]*1000,p[2]*1000,p[3]*1000])
        with open(outputfile,"w") as f:
            json.dump(czml,f,indent=4)
        
        print(f"Succes! Am procesat {len(datapoints)} puncte. Fisier generat: {outputfile}")
    except FileNotFoundError:
        print(f"eroare: nu AM GASIT FISIERELE")

if __name__ == "__main__":
    convert_czml()
