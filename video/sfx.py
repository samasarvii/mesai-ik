import json, math, random, struct, wave, sys
tl = json.load(open(sys.argv[1])); SR=44100; N=int(SR*tl['duration']); buf=[0.0]*N
random.seed(3)
def add(t0, gen, dur):
    s=int(t0*SR)
    for i in range(int(dur*SR)):
        if s+i<N: buf[s+i]+=gen(i/SR)
def pop(t):   # bubbly upward sweep
    f=380+1300*t/0.09; return 0.55*math.sin(2*math.pi*f*t)*math.exp(-t*38)
def tick(t):  # typewriter click
    return 0.32*(random.random()*2-1)*math.exp(-t*900)+0.18*math.sin(2*math.pi*2400*t)*math.exp(-t*400)
def chime(t):
    return sum(0.18*math.sin(2*math.pi*f*t)*math.exp(-t*5) for f in (1318.5,1975.5,2637))
for p in tl['pops']: add(p, pop, .12)
for k in range(tl['typeChars']):
    if 'Benim adım Mesai'[k]!=' ': add(tl['typeStart']+k/tl['cps'], tick, .04)
add(2.85, chime, .9)
peak=max(abs(x) for x in buf); 
with wave.open(sys.argv[2],'w') as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes(b''.join(struct.pack('<h',int(32767*0.85*x/peak)) for x in buf))
