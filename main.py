from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class MainUI(BoxLayout):

    totals = {}

    def calculate(self):
        try:
            name = self.ids.option.text

            a = int(self.ids.a.text)
            b = int(self.ids.b.text)
            c = int(self.ids.c.text)
            d = int(self.ids.d.text)

            total = 0
            steps = ""
            step = 1

            while c > 0:
                value = a * b
                total += value
                steps += f"Step {step}: {a} × {b} = {value}\n"

                a -= 1
                b -= 1
                c -= 1
                step += 1

            total += d

            self.totals[name] = total

            self.ids.result.text = f"{name} = {total}"
            self.ids.steps.text = steps

        except:
            self.ids.result.text = "❌ Invalid Input"

    def add_extra(self):
        try:
            name = self.ids.option.text
            extra = int(self.ids.extra.text)

            if name not in self.totals:
                self.ids.result.text = "❌ Calculate first"
                return

            old = self.totals[name]
            new = old + extra

            self.totals[name] = new

            self.ids.result.text = f"{name} = {new} (+{extra})"

        except:
            self.ids.result.text = "❌ Error"

    def clear_fields(self):
        self.ids.a.text = ""
        self.ids.b.text = ""
        self.ids.c.text = ""
        self.ids.d.text = ""
        self.ids.extra.text = ""
        self.ids.steps.text = ""
        self.ids.result.text = "Result"


class ConeApp(App):
    def build(self):
        return MainUI()


if __name__ == "__main__":
    ConeApp().run()