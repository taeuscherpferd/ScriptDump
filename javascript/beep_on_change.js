((target, text) => {

// Find the element
//const target = document.getElementById("__bolt-status-3444-desc");

// Function to play a beep
function beep() {
    const ctx = new (window.AudioContext || window.webkitAudioContext)();
    const oscillator = ctx.createOscillator();
    oscillator.type = "sine";
    oscillator.frequency.setValueAtTime(1000, ctx.currentTime); // 1000 Hz
    oscillator.connect(ctx.destination);
    oscillator.start();
    oscillator.stop(ctx.currentTime + 0.2); // 0.2 seconds
}

// Observer to watch for changes
const observer = new MutationObserver(mutations => {
    mutations.forEach(mutation => {
        if (mutation.type === "characterData" || mutation.type === "childList") {
            //if (target.textContent.trim() !== "Waiting") {
            if (!target.textContent.trim().includes(text)) {
                beep();
                console.log("Status changed to:", target.textContent.trim());
                observer.disconnect(); // Stop watching after first change
            }
        }
    });
});

// Start observing the element
observer.observe(target, { childList: true, characterData: true, subtree: true });

console.log("Watching for status change...");

})(document.getElementById("__bolt-status-37509-desc"), "Waiting" )
