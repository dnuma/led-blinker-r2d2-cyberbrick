# CyberBrick Alternating LED Snippets

Make CyberBrick LEDs alternate between two colours from a 3-position switch. My inspiration comes from this amazing 3D print project: https://makerworld.com/en/models/1549117-build-a-droid-cyberbrick-based-robot-kit#profileId-1689536

<img width="548" height="986" alt="Adobe Express - WhatsApp Video 2026-08-20 at 10 09 42" src="https://github.com/user-attachments/assets/bdc1a92a-dc04-43be-a8b8-308bc8b545e7" />


The app's LED effects store a single RGB value each, and `blink` toggles that one colour
against off. Two-colour alternation is impossible through the GUI. These snippets do it.

I used [this remote](https://makerworld.com/en/models/2210984-remote-control-for-droid?from=search#profileId-2403494), but it applies to any remote with the 3-pos switch

## Setup

Requires the **desktop** app — mobile can't edit code snippets.

1. Receiver → **Code (BETA)** → **+Add** → **Code Edit** → paste a snippet from `snippets/`.
   Repeat for each.
<img width="1434" height="896" alt="image" src="https://github.com/user-attachments/assets/262f4d7f-edcd-447e-bde2-e7ae26259364" />
   
2. **Remote** → your 3-position switch. Set each row's **Module** to `CODE` and **Value** to
   the matching snippet.
<img width="1433" height="889" alt="image" src="https://github.com/user-attachments/assets/c08ff6e0-bd50-48ee-9edf-477f911e431e" />
  
3. **Save** → **Send to Device**.

`snippets/blink.py` alternates red/white. `solid_red.py` and `solid_white.py` are the other
two positions.

## Gotchas

**The import path in the API docs doesn't work here.** The docs say `bbl.leds`; inside the
snippet sandbox it's `leds`. Wrong path = silent death, no error shown.

**`set_led_effect()` is unreliable from snippets.** Write pixels directly via `led.np[i]`,
and set `led.repeat_count = 0` first or a running GUI effect will fight you.

**Snippets run in isolation with no persistent globals.** They fire once and exit, so
anything continuous needs a `machine.Timer`. `Timer(0)` is hardware, so any snippet can
cancel a timer started by another.

**Every position sharing the LED channel must be a CODE row.** The timer ignores the config
— leave a position on the `LED1` module and the blink will overwrite it 4×/second.

## Limits

- `period=250` in `blink.py` is the blink interval in ms.
- `range(4)` covers OUT1–OUT4. For a second channel, add `LEDController("LED2")` (must be
  enabled in the config).
- Timer-driven snippets add noticeable control latency. If drive response gets mushy, raise
  `period` to 400–500.
- The Code module is BETA and undocumented. Expect breakage across app versions.

## Credits

The `leds` import path, direct-NeoPixel writes, and the Timer pattern come from the
CyberBrick community, notably the
[Code snippet for LED](https://forum.bambulab.com/t/code-snippet-for-led/204530) thread.

