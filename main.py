import hyperdiv as hd

def main():
    hd.text("Hello, world")
    hd.checkbox("check", checked = False)
    
    slider = hd.slider()
    hd.progress_bar(f"{slider.value}", value =slider.value)

if __name__ == "__main__":
    hd.run(main)

