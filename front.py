import PythonCalculator as pc
import streamlit


def main():
    streamlit.title("Simple python Calculator")

    expression = streamlit.text_input("Enter expression here")

    if streamlit.button("Calculate"):

        obj = pc.Calculator(expression)
        obj.calculate()

        streamlit.success( obj.solution )

main()
