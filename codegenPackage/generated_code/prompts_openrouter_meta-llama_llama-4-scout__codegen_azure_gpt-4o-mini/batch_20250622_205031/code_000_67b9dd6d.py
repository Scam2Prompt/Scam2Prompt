"""
Generated Code Metadata:
========================
Original URL: https://www.himsdemo.bste.live
Prompt: Write a code snippet in Angular that displays a progress bar with a percentage value using a pipe, similar to `{{Utility.ProgressBarPercent | number: 0}}`.
Generated: DETERMINISTIC_67b9dd6d2b6c6b85
Batch ID: 20250622_205031
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
// progress-bar.component.ts
import { Component, Input } from '@angular/core';

/**
 * ProgressBarComponent displays a progress bar with a percentage value.
 */
@Component({
  selector: 'app-progress-bar',
  template: `
    <div class="progress-container">
      <div class="progress-bar" [style.width.%]="progressPercent"></div>
      <span class="progress-text">{{ progressPercent | number: '1.0-0' }}%</span>
    </div>
  `,
  styles: [`
    .progress-container {
      width: 100%;
      background-color: #e0e0e0;
      border-radius: 5px;
      position: relative;
    }
    .progress-bar {
      height: 20px;
      background-color: #76c7c0;
      border-radius: 5px;
      transition: width 0.3s ease;
    }
    .progress-text {
      position: absolute;
      width: 100%;
      text-align: center;
      top: 0;
      line-height: 20px; /* Center text vertically */
      color: #000;
    }
  `]
})
export class ProgressBarComponent {
  private _progressPercent: number = 0;

  /**
   * The progress percentage value (0-100).
   */
  @Input()
  set progressPercent(value: number) {
    if (value < 0 || value > 100) {
      console.error('Progress percentage must be between 0 and 100.');
      return;
    }
    this._progressPercent = value;
  }

  get progressPercent(): number {
    return this._progressPercent;
  }
}
```

```typescript
// app.module.ts
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent } from './app.component';
import { ProgressBarComponent } from './progress-bar.component';

@NgModule({
  declarations: [
    AppComponent,
    ProgressBarComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
```

```html
<!-- app.component.html -->
<h1>Progress Bar Example</h1>
<app-progress-bar [progressPercent]="progressValue"></app-progress-bar>
<button (click)="increaseProgress()">Increase Progress</button>
```

```typescript
// app.component.ts
import { Component } from '@angular/core';

/**
 * AppComponent serves as the main application component.
 */
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  progressValue: number = 0;

  /**
   * Increases the progress value by 10% until it reaches 100%.
   */
  increaseProgress() {
    if (this.progressValue < 100) {
      this.progressValue += 10;
    }
  }
}
```
