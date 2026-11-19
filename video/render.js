const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const [,, outDir, onlyTimes] = process.argv;
  fs.mkdirSync(outDir, { recursive: true });
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  await p.goto('file://' + __dirname + '/scene.html');
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(500);
  const fps = 30, dur = 6.0;
  const times = onlyTimes ? onlyTimes.split(',').map(Number) : [...Array(Math.round(fps*dur)).keys()].map(i => i/fps);
  for (let i = 0; i < times.length; i++) {
    await p.evaluate(t => window.render(t), times[i]);
    await p.screenshot({ path: `${outDir}/f${String(i).padStart(4,'0')}.png` });
  }
  fs.writeFileSync(outDir + '/timeline.json', JSON.stringify(await p.evaluate(() => window.TIMELINE)));
  await b.close();
})();
