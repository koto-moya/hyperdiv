import hyperdiv as hd
import numpy as np

def main():
    hd.text("Hello, world")
    hd.checkbox("check", checked = False)
    
    slider = hd.slider()
    hd.progress_bar(f"{slider.value}", value =slider.value)

    button = hd.button("cos")
    if button.clicked:
        x = [float(x) for x in np.arange(0,10,.01)]
        y = [float(np.cos(xs)) for xs in x]
        data = list(zip(x,y))
        hd.line_chart(data)



if __name__ == "__main__":
    hd.run(main)

