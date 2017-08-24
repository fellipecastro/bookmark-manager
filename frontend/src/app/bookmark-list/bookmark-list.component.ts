import { Component, OnInit } from '@angular/core';

import { Bookmark } from './../bookmark';
import { BookmarkService } from './../bookmark.service';
import { LoginService } from './../login.service';

@Component({
  selector: 'bookmark-list',
  templateUrl: './bookmark-list.component.html',
  styleUrls: ['./bookmark-list.component.css']
})
export class BookmarkListComponent implements OnInit {
  title = 'Bookmark Manager';
  bookmarks: Bookmark[];
  selectedBookmark: Bookmark;

  constructor(
    private bookmarkService: BookmarkService,
    private loginService: LoginService
  ) { }

  getBookmarks(): void {
    this.bookmarkService.getBookmarks().subscribe(bookmarks => this.bookmarks = bookmarks);
  }

  ngOnInit(): void {
    this.getBookmarks();
  }

  onSelect(bookmark: Bookmark): void {
    this.selectedBookmark = bookmark;
  }
}
