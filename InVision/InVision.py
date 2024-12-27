import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

class Section(BoxLayout):
    """Custom section with a border and a title."""
    def __init__(self, title, **kwargs):
        super().__init__(orientation="vertical", padding=10, **kwargs)
        self.add_widget(Label(text=title, font_size=30, halign="center"))

class RegressionTool(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(cols=1, spacing=10, padding=10, **kwargs)

        # Add Title "ML Regression Tool" at the top center
        title_label = Label(
            text="InVision",
            font_size=40,
            size_hint=(1, None),
            height=60,
            halign="center",
            valign="middle"
        )
        sub_title_label = Label(
            text="Machine Learning Regression Tool - KSHITIJ K SAWANT",
            font_size=20,  # Smaller font size for subtitle
            size_hint=(1, None),
            height=40,
            halign="center",
            valign="middle"
        )
        self.add_widget(title_label)
        self.add_widget(sub_title_label)

        # Main Layout with Two Columns
        main_layout = GridLayout(cols=2, spacing=10, size_hint=(1, 1))

        # Left: CSV Details and Feature/Target Selection
        left_section = BoxLayout(orientation="vertical", spacing=10, padding=10, size_hint=(1, 1))

        # CSV Section
        csv_section = Section("CSV File Column Details & Target Selection")
        self.target_button_layout = GridLayout(cols=2, spacing=5, size_hint=(1, None), height=200)
        csv_section.add_widget(self.target_button_layout)
        left_section.add_widget(csv_section)

        # Feature Selection
        feature_section = Section("Select Features")
        self.features_button_layout = GridLayout(cols=2, spacing=5, size_hint=(1, None), height=200)
        feature_section.add_widget(self.features_button_layout)
        left_section.add_widget(feature_section)

        main_layout.add_widget(left_section)

        # Right: Results and Run Button Section
        right_section = BoxLayout(orientation="vertical", spacing=10, padding=10, size_hint=(1, 1))

        # Drag and Drop Section Label Only
        drag_section_label = Label(
            text="Drag and Drop CSV File Here",
            size_hint=(1, None),
            height=50,
            font_size=30,
            halign="center",
            valign="middle"
        )
        right_section.add_widget(drag_section_label)

        # Run Button and Results Section
        self.run_button = Button(
            text="Run Regression",
            size_hint=(1, None),
            height=50,
            font_size=25,
            pos_hint={"center_x": 0.5}
        )
        self.run_button.bind(on_press=self.run_regression)
        right_section.add_widget(self.run_button)

        self.results_label = Label(
            text="Suggested Features and Target will display here",
            halign="left",
            valign="top",
            size_hint=(1, 1),
            font_size=35
        )
        results_scroll = ScrollView(size_hint=(1, 1))
        results_scroll.add_widget(self.results_label)
        right_section.add_widget(results_scroll)

        main_layout.add_widget(right_section)

        self.add_widget(main_layout)

        # Data and Event Bindings
        self.data = None
        self.selected_features = []
        self.target_columns = []
        Window.size = (1024, 576)  # Set the window size to a 16:9 ratio
        Window.bind(on_dropfile=self.on_file_drop)

    def on_file_drop(self, window, file_path):
        """Handle drag-and-drop file events."""
        self.load_csv_from_path(file_path.decode("utf-8"))

    def load_csv_from_path(self, file_path):
        """Load the selected CSV file and populate feature/target options."""
        try:
            self.data = pd.read_csv(file_path)
            self.display_suggestions()
            self.features_button_layout.clear_widgets()
            self.target_button_layout.clear_widgets()

            # Populate features as buttons
            for column in self.data.columns:
                feature_btn = Button(text=column, size_hint=(1, None), height=40, font_size=16)
                feature_btn.bind(on_press=lambda btn, col=column: self.toggle_feature(col, btn))
                self.features_button_layout.add_widget(feature_btn)

                # Populate target buttons
                target_btn = Button(text=column, size_hint=(1, None), height=40, font_size=16)
                target_btn.bind(on_press=lambda btn, col=column: self.toggle_target(col, btn))
                self.target_button_layout.add_widget(target_btn)

        except Exception as e:
            self.results_label.text = f"Error loading CSV: {e}"

    def display_suggestions(self):
        """Display suggested features and target columns in the results area."""
        try:
            suggested_features = ", ".join(self.data.columns[:3])
            suggested_target = self.data.columns[-1]
            self.results_label.text = f"Suggested Features: {suggested_features}\nSuggested Target: {suggested_target}"
        except Exception as e:
            self.results_label.text = f"Error displaying suggestions: {e}"

    def toggle_feature(self, column, button):
        """Add or remove selected features."""
        try:
            if column in self.selected_features:
                self.selected_features.remove(column)
                button.background_color = (1, 1, 1, 1)  # Default color
            else:
                self.selected_features.append(column)
                button.background_color = (0, 1, 0, 1)  # Highlighted color
        except Exception as e:
            self.results_label.text = f"Error toggling feature: {e}"

    def toggle_target(self, column, button):
        """Add or remove selected target columns with green tint toggle."""
        try:
            if column in self.target_columns:
                self.target_columns.remove(column)
                button.background_color = (1, 1, 1, 1)  # Default color
            else:
                self.target_columns.append(column)
                button.background_color = (0, 1, 0, 1)  # Highlighted color
            self.update_target_display()
        except Exception as e:
            self.results_label.text = f"Error toggling target: {e}"

    def update_target_display(self):
        """Update the display of selected target columns."""
        try:
            target_display = ", ".join(self.target_columns)
            self.results_label.text = f"Selected Targets: {target_display}"
        except Exception as e:
            self.results_label.text = f"Error updating target display: {e}"

    def run_regression(self, instance): 
        """Perform regression and display results."""
        try:
            # Check if data is loaded, features are selected, and target columns are selected
            if self.data is None or self.data.empty:
                self.results_label.text = "Error: No data loaded. Please upload a valid CSV file."
                return
            if not self.selected_features:
                self.results_label.text = "Error: Select at least one feature column."
                return
            if not self.target_columns:
                self.results_label.text = "Error: Select at least one target column."
                return

            # Drop rows with missing values in selected features and target columns
            data = self.data.dropna(subset=self.selected_features + self.target_columns)

            # Prepare features and target for regression
            X = data[self.selected_features]
            y = data[self.target_columns]

            # Split data into training and testing sets
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            # Train the regression model
            model = LinearRegression()
            model.fit(X_train, y_train)

            # Make predictions and calculate metrics
            y_pred = model.predict(X_test)
            mse = mean_squared_error(y_test, y_pred)
            r2 = r2_score(y_test, y_pred)

            # Display regression results
            self.results_label.text = f"Regression Results:\nMSE: {mse:.2f}\nR²: {r2:.4f}"
        except Exception as e:
            self.results_label.text = f"Error running regression: {e}"


class RegressionApp(App):
    def build(self):
        self.title = "InVision - Machine Learning Regression Tool"
        Window.set_icon('InVision Logo.png')
        return RegressionTool()

if __name__ == "__main__":
    RegressionApp().run()
